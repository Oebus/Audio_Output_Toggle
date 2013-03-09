import subprocess, os
from pyhk import pyhk
from _winreg import *

#GLOBALS
# set this to the location of your downloaded setDefaultAudioDevice.exe file
PATH_TO_SETDEFAULTDEVICE = "C:\\Program Files (x86)\\Audio Device Toggle\\SetDefaultAudioDevice.exe"
# set the device IDs and device names specific to your system
DEVICE_IDS = {"device_1": tuple(["optical_out","{cd57ae33-2d9f-435f-bdcd-a68224d92444}"]),"device_2": tuple(["speakers","{87bb8316-ed38-424c-9593-1805aec9c8a0}"])}
# choose a key combination by changing this list, or keep it the same
HOTKEYCOMBO = ['Ctrl', 'Shift', 'Alt', '1']

def ToggleAudioOutput():
    if GetCurrentDevice()==DEVICE_IDS["device_1"][0]:
        SetCurrentDevice("device_2")
    else:
        SetCurrentDevice("device_1")

def GetCurrentDevice():
    aKey = CreateKeyEx(HKEY_LOCAL_MACHINE, "Software\\Audio Device Toggle\\", 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS) 

    try:
        current_device = QueryValueEx(aKey, "current_device")[0]
    except:
        SetValueEx(aKey, "current_device", 0, REG_SZ, DEVICE_IDS["device_1"][0])
        current_device = DEVICE_IDS["device_1"][0]

    return current_device

def SetCurrentDevice(target_device):
    subprocess.call("\""+PATH_TO_SETDEFAULTDEVICE+"\""+" "+DEVICE_IDS[target_device][1]+" multimedia", shell=True)

    aKey = CreateKeyEx(HKEY_LOCAL_MACHINE, "Software\\Audio Device Toggle\\", 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS) 
    SetValueEx(aKey, "current_device", 0, REG_SZ, DEVICE_IDS[target_device][0])

hot = pyhk()
hot.getHotkeyListNoSingleNoModifiers()
id1 = hot.addHotkey(HOTKEYCOMBO,ToggleAudioOutput)
hot.start()