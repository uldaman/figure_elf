import pyHook
import pythoncom
from .script.macro import (
    key_up_macro,
    key_down_macro,
)


def on_key_up_event(event):
    if event.WindowName.startswith("逆水寒"):
        key_up_macro(event.Key)  # 需要优化成按住一直触发
    return True


def on_key_down_event(event):
    if event.WindowName.startswith("逆水寒"):
        key_down_macro(event.Key)
    return True


hookMgr = pyHook.HookManager()
hookMgr.KeyUp = on_key_up_event
hookMgr.KeyDown = on_key_down_event
hookMgr.HookKeyboard()
pythoncom.PumpMessages()
