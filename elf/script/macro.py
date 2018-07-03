from .测试 import 测试
from .冲劲寸拳 import 冲劲寸拳


def key_up_macro(key):
    macro_up.get(key, lambda: None)()


def key_down_macro(key):
    macro_down.get(key, lambda: None)()


macro_up = {
    "Q": lambda: 测试.execution()
}


macro_down = {
    "Q": lambda: 冲劲寸拳.execution()
}
