# -*- coding: utf-8 -*-
#Copyright (C) Ibrahim Hamadeh, released under GPLv2.0
#See the file COPYING for more details.
#This addon is aimed to get meaning of words using almaany.com website dictionaries.
#press nvda+windows+d, a dialog will be displayed, and you will be standing on an edit box
#write the word you want, tab and choose the dictionary, press enter and the meaning will be displayed in a separate browseable message box.

import gui, wx
from gui import guiHelper
import config
import globalPluginHandler
from .myDialog import MyDialog
from logHandler import log
import addonHandler
addonHandler.initTranslation()

#default configuration 
configspec={
	"windowType": "integer(default=0)",
	"closeDialogAfterRequiringTranslation": "boolean(default= False)"
}
config.conf.spec["dictionariesAlmaany"]= configspec

INSTANCE= None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory= _('Dictionaries Almaany')

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)

		if hasattr(gui, 'SettingsPanel'):
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(DictionariesAlmaany)
		else:
			self.prefmenu= gui.mainFrame.sysTrayIcon.preferencesMenu
			self.addonmenu= self.prefmenu.Append(wx.ID_ANY,
			# Translators: label of Dictionaries Almaany setting menu in preferences menu
			_("&Dictionaries Almaany..."),
			"Opens setting dialog"
			)
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onOpenSettingDialog, self.addonmenu)

	def onOpenSettingDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(DictionariesAlmaany)

	def terminate(self):
		if hasattr(gui, 'SettingsPanel'):
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(DictionariesAlmaany)
		else:
			try:
				self.prefmenu.RemoveItem(self.addonmenu)
			except :
				pass

	def script_showDialog(self, gesture):
		global INSTANCE
		if not INSTANCE:
			d= MyDialog(gui.mainFrame)
			#d= MyDialog(None)
#			log.info('after creating object')
			d.postInit()
			d.Raise()
			d.Show()
			INSTANCE= d
		else:
			INSTANCE.Raise()
	script_showDialog.__doc__= _('Opens DictionariesAlmaany dialog to get meaning of words.')

	__gestures= {
	'kb:nvda+windows+d': 'showDialog'
	}

parentClass= gui.SettingsPanel if hasattr(gui, 'SettingsPanel') else gui.SettingsDialog
#make either SettingsPanel or SettingsDialog class
class DictionariesAlmaany(parentClass):
	# Translators: title of the dialog
	title= _("Dictionaries Almaany")

	def makeSettings(self, sizer):
		settingsSizerHelper = guiHelper.BoxSizerHelper(self, sizer=sizer)

		# Translators: Type of windows to display translation result.
		windowTypes= [_("Default full browser"), _("Browser window only"), _("NVDA browseable message box(choose it after testing)")]
		self.resultWindowComboBox= settingsSizerHelper.addLabeledControl(
		# Translators: label of cumbo box to choose type of window to display result.
		_("Choose type of window To Display Result:"), 
		wx.Choice, choices= windowTypes)
		self.resultWindowComboBox.SetSelection(config.conf["dictionariesAlmaany"]["windowType"])

		# Translators: label of the check box 
		self.closeDialogCheckBox=wx.CheckBox(self,label=_("&Close Dictionaries Almaany Dialog after requiring translation"))
		self.closeDialogCheckBox.SetValue(config.conf["dictionariesAlmaany"]["closeDialogAfterRequiringTranslation"])
		settingsSizerHelper.addItem(self.closeDialogCheckBox)

	if hasattr(parentClass, 'onSave'):
		def onSave(self):
			config.conf["dictionariesAlmaany"]["windowType"]= self.resultWindowComboBox.GetSelection()
			config.conf["dictionariesAlmaany"]["closeDialogAfterRequiringTranslation"]= self.closeDialogCheckBox.IsChecked() 

	else:
		def onOk(self, evt):
			config.conf["dictionariesAlmaany"]["windowType"]= self.resultWindowComboBox.GetSelection()
			config.conf["dictionariesAlmaany"]["closeDialogAfterRequiringTranslation"]= self.closeDialogCheckBox.IsChecked() 
			super(DictionariesAlmaany, self).onOk(evt)

		def postInit(self):
			self.resultWindowComboBox.SetFocus()

