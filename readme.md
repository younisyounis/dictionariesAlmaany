# Dictionaries Almaany #

Author: Ibrahim Hamadeh  
Contributors: Abdel  
Download [version 2.2][1]  

This addon helps you get the meaning of single words through the almaany.com website.  
[almaany.com](https://www.almaany.com/en/dict/ar-en/ "With a Title").

notice: All dictionaries used are bilingual, meaning that for instance, the arabic english dictionary translates from arabic to english and from english to arabic also. 

***

## Usage

*	Press nvda+windows+d, dictionaries almaany dialog will be displayed  
and you will be standing on an edit field  
if when pressing this command, you were standing on a selected word, the word will be put in the edit field  
*	otherwise, enter in the edit field the word you want, tab an choose the dictionary you want and press enter on it.  
if you want to get the meaning in the default Arabic to Arabic dictionary, you can always press enter on the edit field and after that the meaning of the word will be displayed in a separate browseable window.  
*	You can moreover, going to addon's setting dialog, through:  
NVDA menu/preferences/Settings/dictionaries almaany  
from there, you can choose the type of window used to display the meaning.  
the default and first choice, is a browser like window as in firefox or google chrome, it is a browser window without file menus or address brar.  
please remember you can close this window only, with control+w or alt+f4.  
the other is the native NVDA message box, used it only after testing and if it suits you, for in our experience it smetimes make NVDA freezes.  
*	From that setting dialog, you can also choose whether to close Dictionaries Almaany dialog after requesting the meaning of word or not.  
 
## Changes for 2.1 .

*	Make setting dialog for the addon  
*	Give the user the choice to get the result in browser window in kiosk mode, like chrome or firefox, full screen without menus or address bar.  
*	Give the user the option to close Dictionaries Almaany dialog after requesting translation.  

## Changes for 2.0 .

*	Added compatibility with versions of NVDA using Python 3.

## Changes for 1.1 ##

fixing some bugs, getting the addon to return to work after it has stopped working from the server  

*	using urllib2 to make a request object  
*	add user-agent to the request headers.  

## Changes for 1.0 ##

*	Initial version.

### Contributions ###

*	Thanks to Abdel contribution for porting the addon to python3, and using last nvda addon template.  

[1]: https://github.com/ibrahim-h/dictionariesAlmaany/releases/download/2.2/DictionariesAlmaany-2.2.nvda-addon