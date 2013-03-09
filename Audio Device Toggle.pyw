import subprocess, os
from pyhk import pyhk
from _winreg import *

PATH_TO_SETDEFAULTDEVICE = "C:\\Program Files (x86)\\Audio Device Toggle\\SetDefaultAudioDevice.exe"
DEVICE_IDS = {"optical_out":"{cd57ae33-2d9f-435f-bdcd-a68224d92444}","speakers":"{87bb8316-ed38-424c-9593-1805aec9c8a0}"}

def ToggleAudioOutput():
    if GetCurrentDevice()=="optical_out":
        SetCurrentDevice("speakers")
    else:
        SetCurrentDevice("optical_out")

def GetCurrentDevice():
    aKey = CreateKeyEx(HKEY_LOCAL_MACHINE, "Software\\Audio Device Toggle\\", 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS) 

    try:
        current_device = QueryValueEx(aKey, "current_device")[0]
    except:
        SetValueEx(aKey, "current_device", 0, REG_SZ, "optical_out")
        current_device = "optical_out"

    return current_device

def SetCurrentDevice(target_device):
    global PATH_TO_SETDEFAULTDEVICE, DEVICE_IDS

    subprocess.call("\""+PATH_TO_SETDEFAULTDEVICE+"\""+" "+DEVICE_IDS[target_device]+" multimedia", shell=True)

    aKey = CreateKeyEx(HKEY_LOCAL_MACHINE, "Software\\Audio Device Toggle\\", 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS) 
    SetValueEx(aKey, "current_device", 0, REG_SZ, target_device)

hot = pyhk()
hot.getHotkeyListNoSingleNoModifiers()
id1 = hot.addHotkey(['Ctrl', 'Shift', 'Alt', '1'],ToggleAudioOutput)
hot.start()


'''
PyInstaller Build Command

<path to 32-bit python> pyinstaller.py -F -w -i <path to icon file> <path to .pyw file

* -F is for one-file compile, so that instsrv and srvany can install as windows service
** -w, saving as .pyw, and using subprocess with shell=True ensures no cmd popups
'''