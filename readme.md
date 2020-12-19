# Dictionaries Almaany #

Author: Ibrahim Hamadeh  

This addon helps you get the meaning of single words through the almaany.com website.  
[almaany.com](https://www.almaany.com/en/dict/ar-en/ "With a Title").

notice: All dictionaries used are bilingual, meaning that for instance, the arabic english dictionary translates from arabic to english and from english to arabic also. 

***

## Usage

*	Press nvda+windows+d, dictionaries almaany dialog will be displayed  
and you will be standing on an edit field  
if when pressing this command, you were standing on a selected word, the word will be put in the edit field  
*	otherwise, enter in the edit field the word you want, tab an choose the dictionary you want and press enter on it.  
if you want to get the meaning in the default Arabic to Arabic dictionary, you can always press enter on the edit field and after that the meaning of the word will be displayed in a separate browseable message box.

## Changes for 2.0 .

* Added compatibility with versions of NVDA using Python 3.

## Changes for 1.1 ##

fixing some bugs, getting the addon to return to work after it has stopped working from the server  

*	using urllib2 to make a request object  
*	add user-agent to the request headers.  

## Changes for 1.0 ##

*	Initial version.