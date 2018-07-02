import pythoncom
import pyHook
from .macro import cast


def onKeyboardEvent(event):
    # 监听键盘事件
    if event.WindowName.startswith("逆水寒"):
        if event.Key == 'Q':
            cast()
            return False
    return True


hookMgr = pyHook.HookManager()
hookMgr.KeyDown = onKeyboardEvent  # 按下不放时，能一直触发
hookMgr.HookKeyboard()
pythoncom.PumpMessages()
