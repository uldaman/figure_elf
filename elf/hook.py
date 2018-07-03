import pyHook
import pythoncom
from .script.macro import (
    match_key_up_func,
    match_key_down_func,
)


def on_key_up_event(event):
    if event.WindowName.startswith("逆水寒"):
        func = match_key_up_func(event.Key)
        if func:
            func()
    return True


def on_key_down_event(event):
    if event.WindowName.startswith("逆水寒"):
        func = match_key_down_func(event.Key)
        if func:
            func()
    return True


hookMgr = pyHook.HookManager()
hookMgr.KeyUp = on_key_up_event
hookMgr.KeyDown = on_key_down_event
hookMgr.HookKeyboard()
pythoncom.PumpMessages()
