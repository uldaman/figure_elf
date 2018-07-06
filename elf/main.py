import time
import pyHook
import threading
import pythoncom
from .script import KeyHandler
from .hook import (
    on_key_down_event,
    on_key_up_event,
)


def key_down_loop():
    while True:
        KeyHandler.handle_key_down()
        time.sleep(1 / 16)


def main():
    threading.Thread(target=key_down_loop, name='key_down_loop').start()
    hookMgr = pyHook.HookManager()
    hookMgr.KeyDown = on_key_down_event
    hookMgr.KeyUp = on_key_up_event
    hookMgr.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    main()
