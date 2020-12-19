# -*- coding: utf-8 -*-
#Ibrahim Hamadeh
#This addon is aimed to get meaning of words using almaany.com website dictionaries.
#This addon is under GNU GENERAL PUBLIC LICENSE
#press nvda+windows+d, a dialog will be displayed, and you will be standing on an edit box
#write the word you want, tab and choose the dictionary, press enter and the meaning will be displayed in a separate browseable message box.

import gui
import globalPluginHandler
from .myDialog import MyDialog
from logHandler import log
import addonHandler
addonHandler.initTranslation()

INSTANCE= None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory= _('Dictionaries Almaany')

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