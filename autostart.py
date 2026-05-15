# autostart.py — Add/remove Scryptian from Windows startup

import sys
import os
import winreg


def _get_exe_path():
    """Get path to current executable (works for both .py and .exe)."""
    if getattr(sys, 'frozen', False):
        return sys.executable
    return f'pythonw "{os.path.abspath("main.py")}"'


_KEY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"


def enable():
    """Add Scryptian to Windows startup via registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, _KEY_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Scryptian", 0, winreg.REG_SZ, _get_exe_path())
        winreg.CloseKey(key)
    except Exception:
        pass


def is_enabled():
    """Check if registry entry exists with correct path."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, _KEY_PATH, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, "Scryptian")
        winreg.CloseKey(key)
        return value == _get_exe_path()
    except Exception:
        return False
