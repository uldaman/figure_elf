from .测试 import 测试
from .冲劲寸拳 import 冲劲寸拳


def match_key_up_func(key):
    return macro_up.get(key, None)


def match_key_down_func(key):
    return macro_down.get(key, None)


macro_up = {
    "Q": lambda: 测试.execution()
}


macro_down = {
    "Q": lambda: 冲劲寸拳.execution()
}
