##################
#   File Info    #
##################
Audio Device Toggle.pyw
Author: Matthew Simons
Date: 3/9/2013

Python version 2.7.3
Platform: Windows 7
Imports: pywin32, pyHook, pyhk
Uses Externally: setDefaultAudioDevice.exe (see resources section for download link)
Packages with: pyInstaller

##################
#     Usage      #
##################

This program runs silently in the background, awaiting a user-defined key combination. When the combination is pressed, setDefaultAudioDevice.exe is run and given the device ID of an audio device, which it sets as the default audio device for multimedia. A registry key keeps track of the current default device, and setDefaultAudioDevice.exe resides within the same directory as the compiled "Audio Device Toggle.exe".

To install:
	-get/install prereqs (resources listed below)
	-change the global variables at the beginning of the script
		-set the location of your downloaded setDefaultAudioDevice.exe
		-get your audio device IDs from the registry and put them into the 
			dictionary object
		-set your hotkey combo (or don't and keep the default)
	-use pyInstaller to build your .exe (strictly speaking this is optional unless
		you want to install this later as a windows service)
	-add a shortcut to your .exe within the startup folder, or install it as a 
		windows service
	-Success! Spam your toggle hotkey to your heart's content

PyInstaller Build Command
``````````````````````````
<path to 32-bit python> pyinstaller.py -F -w -i <path to icon file> <path to .pyw file>

* -F is for one-file compile, so that instsrv and srvany can install as windows service
** -w, saving as .pyw, and using subprocess with shell=True ensures no cmd popups

#############
# Resources #
#############

Package	- URL		
````````````````````
pythoncom (pywin32) - http://sourceforge.net/projects/pywin32/			
pyHook - http://sourceforge.net/projects/pyhook/?source=dlp	
pyhk - https://code.google.com/p/pyhk/source/browse/trunk/pyhk.py
setDefaultAudioDevice - http://zornsoftware.codenature.info/free-downloads?did=1
pyInstaller - http://www.pyinstaller.org/							

*All resources provided under open source licensing