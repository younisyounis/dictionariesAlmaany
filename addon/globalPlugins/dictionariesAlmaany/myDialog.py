# -*- coding: utf-8 -*-
#This module is responsible for displaying dictionaries almaany dialog

import wx
import queueHandler
import config
import sys
#import webbrowser
from .fetchtext import MyThread
from .fetchtext import isSelectedText
from .getbrowsers import getBrowsers
from tones import beep
import time
import subprocess
import threading
import tempfile
import ui
import os
import addonHandler
addonHandler.initTranslation()
if sys.version_info.major == 2:
	import io
	open = io.open
#browsers as dictionary with label as key, and executable path as value.
browsers= getBrowsers()

def appIsRunning(app):
	'''Checks if specific app is running or not.
	'''
	processes= subprocess.check_output('tasklist', shell=True).decode('mbcs')
	return app in processes

def openBrowserWindow(label, meaning, directive):
	html= """
	<!DOCTYPE html>
	<meta charset=utf-8>
	<title>{title}</title>
	<meta name=viewport content='initial-scale=1.0'>
	""".format(title= _('Dictionaries Almaany')) + meaning 
	temp= tempfile.NamedTemporaryFile(delete=False)
	path = temp.name + ".html"
	f = open(path, "w", encoding="utf-8")
	f.write(html)
	f.close()
	subprocess.Popen(browsers[label] + directive + path)
	#webbrowser.open(path)
	t=threading.Timer(30.0, os.remove, [f.name])
	t.start()

#dictionaries url
dictionaries_url= ['http://www.almaany.com/ar/dict/ar-ar/', 'http://www.almaany.com/ar/dict/ar-en/',
'http://www.almaany.com/ar/dict/ar-fr/', 'https://www.almaany.com/en/dict/en-en/',
'http://www.almaany.com/ar/dict/ar-es/',
'http://www.almaany.com/ar/dict/ar-tr/', 'http://www.almaany.com/ar/dict/ar-fa/',
'http://www.almaany.com/ar/name/'
]

class MyDialog(wx.Dialog):
	def __init__(self, parent,  word=""):
		super(MyDialog, self).__init__(parent, title = 'Dictionaries Almaany', size = (300, 500))
		self.word= word
		#list of available dictionaries
		self.dictionaries= [u'معجم عربي عربي', u'قاموس عربي إنجليزي',
		u'قاموس عربي فرنسي', u'قاموس إنجليزي إنجليزي',
		u'قاموس عربي ⇔ إسباني',
		u'قاموس عربي ⇔ تركي', u'قاموس عربي ⇐ فارسي',
		u'معاني الأسماء']
		panel = wx.Panel(self, -1)
		editTextLabel= wx.StaticText(panel, -1, _("Enter a word please"))
		editBoxSizer =  wx.BoxSizer(wx.HORIZONTAL)
		editBoxSizer.Add(editTextLabel, 0, wx.ALL, 5)
		self.editTextControl= wx.TextCtrl(panel)
		editBoxSizer.Add(self.editTextControl, 1, wx.ALL|wx.EXPAND, 5)

		cumboSizer= wx.BoxSizer(wx.HORIZONTAL)
		cumboLabel= wx.StaticText(panel, -1, _("Choose Dictionary"))
		cumboSizer.Add(cumboLabel, 0, wx.ALL, 5)
		self.cumbo= wx.Choice(panel, -1, choices= self.dictionaries)
		cumboSizer.Add(self.cumbo, 1, wx.EXPAND|wx.ALL, 5)

		buttonSizer = wx.BoxSizer(wx.VERTICAL)
		self.ok= wx.Button(panel, -1, _('OK'))
		self.ok.SetDefault()
		self.ok.Bind(wx.EVT_BUTTON, self.onOk)
		buttonSizer.Add(self.ok, 0,wx.ALL, 10)
		self.cancel = wx.Button(panel, wx.ID_CANCEL, _('cancel'))
		self.cancel.Bind(wx.EVT_BUTTON, self.onCancel)
		buttonSizer.Add(self.cancel, 0, wx.EXPAND|wx.ALL, 10)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(editBoxSizer, 1, wx.EXPAND|wx.ALL, 10)
		mainSizer.Add(cumboSizer, 1, wx.EXPAND|wx.ALL,10)
		mainSizer.Add(buttonSizer, 0, wx.EXPAND|wx.ALL, 5)
		panel.SetSizer(mainSizer)
	def postInit(self):
		if isSelectedText():
			self.editTextControl.SetValue(isSelectedText())
		self.cumbo.SetSelection(0)
		self.editTextControl.SetFocus()

	def getMeaning(self, text, base_url):
		t= MyThread(text, base_url)
		t.start()
#			while t.isAlive:
		while not t.meaning and not t.error:
			beep(500, 100)
			time.sleep(0.5)
		t.join()


		title= u'المَعَاني message box'
		useBrowserWindow= config.conf["dictionariesAlmaany"]["windowType"]== 0
		useNvdaMessageBox= config.conf["dictionariesAlmaany"]["windowType"]== 1
		if t.meaning and useBrowserWindow:
			if 'Firefox' in browsers and not appIsRunning('firefox.exe'):
				openBrowserWindow('Firefox', t.meaning, directive= ' --kiosk ')
			elif 'Google Chrome' in browsers and not appIsRunning('chrome.exe'):
				openBrowserWindow('Google Chrome', t.meaning, directive= ' -kiosk ')
			elif 'Internet Explorer' in browsers:
				openBrowserWindow('Internet Explorer', t.meaning, directive= ' -k -private ')
		elif t.meaning and useNvdaMessageBox:
			queueHandler.queueFunction(queueHandler.eventQueue, ui.browseableMessage, t.meaning, title=title, isHtml=True)
			return
		elif t.error:
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, _("Sorry, Service not available({})".format(t.error)))

	def onOk(self, e):
		word= self.editTextControl.GetValue()
		if not word:
			self.editTextControl.SetFocus()
			return
		else:
			i= self.cumbo.GetSelection()
			dict_url= dictionaries_url[i]
			self.getMeaning(word, dict_url)
			#wx.CallAfter(self.getMeaning, word, dict_url)
			closeDialogAfterRequiringTranslation= config.conf["dictionariesAlmaany"]["closeDialogAfterRequiringTranslation"]
			if closeDialogAfterRequiringTranslation:
				wx.CallLater(4000, self.Destroy)

	def onCancel (self, e):
		self.Destroy()
