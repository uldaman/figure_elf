from .script import get_key_handler


def on_key_down_event(event):
    if event.WindowName and event.WindowName.startswith("逆水寒"):
        get_key_handler(event.Key)(True)
    return True


def on_key_up_event(event):
    if event.WindowName and event.WindowName.startswith("逆水寒"):
        get_key_handler(event.Key)(False)
    return True
