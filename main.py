import time
import sys
import os
import traceback
import ctypes
from ctypes import wintypes
import win32con
import win32api
import win32gui
import win32process

from spotify import spotify
from sanitizeInput import sanitizer

spotify = spotify()
sanitizer = sanitizer()

lastWindowTitle = ""


def enumWindowsProc(hwnd, lParam):
    global currentWindowTitle
    if (lParam is None) or ((lParam is not None) and (win32process.GetWindowThreadProcessId(hwnd)[1] == lParam)):
        text = win32gui.GetWindowText(hwnd)
        if text:
            wStyle = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)
            if wStyle & win32con.WS_VISIBLE:
                #print("%s" % (text))
                # return text
                currentWindowTitle = text


def enumProcWnds(pid=None):
    win32gui.EnumWindows(enumWindowsProc, pid)


def enumProcs(procName=None):
    pids = win32process.EnumProcesses()
    if procName is not None:
        bufLen = 0x100

        _OpenProcess = ctypes.cdll.kernel32.OpenProcess
        _OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        _OpenProcess.restype = wintypes.HANDLE

        _GetProcessImageFileName = ctypes.cdll.psapi.GetProcessImageFileNameA
        _GetProcessImageFileName.argtypes = [
            wintypes.HANDLE, wintypes.LPSTR, wintypes.DWORD]
        _GetProcessImageFileName.restype = wintypes.DWORD

        _CloseHandle = ctypes.cdll.kernel32.CloseHandle
        _CloseHandle.argtypes = [wintypes.HANDLE]
        _CloseHandle.restype = wintypes.BOOL

        filteredPids = ()
        for pid in pids:
            try:
                hProc = _OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, pid)
            except:
                print("Process [%d] couldn't be opened: %s" %
                      (pid, traceback.format_exc()))
                continue
            try:
                buf = ctypes.create_string_buffer(bufLen)
                _GetProcessImageFileName(hProc, buf, bufLen)
                if buf.value:
                    name = buf.value.decode().split(os.path.sep)[-1]
                    # print name
                else:
                    _CloseHandle(hProc)
                    continue
            except:
                print("Error getting process name: %s" %
                      traceback.format_exc())
                _CloseHandle(hProc)
                continue
            if name.lower() == procName.lower():
                filteredPids += (pid,)
        return filteredPids
    else:
        return pids


def getWindowTitle():
    pids = enumProcs("spotify.exe")
    # print(pids)
    for pid in pids:
        # print(pid)
        # print(enumProcWnds(int(pid)))
        return enumProcWnds(int(pid))


getWindowTitle()
lastWindowTitle = currentWindowTitle

while True:
    if lastWindowTitle == currentWindowTitle:
        getWindowTitle()
        time.sleep(1)
    else:
        lastWindowTitle = currentWindowTitle
        track_id = spotify.search(sanitizer.sanitize(currentWindowTitle))
        spotify.download_art(track_id)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current Song: {currentWindowTitle}")
        time.sleep(1)
