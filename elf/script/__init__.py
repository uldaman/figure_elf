from .群攻 import 群攻


class KeyHandler(object):
    q_down = False

    @classmethod
    def handl_q(cls, is_down):
        cls.q_down = is_down

    @classmethod
    def handle_key_down(cls):
        if cls.q_down:
            群攻.execution()


def get_key_handler(key_vk):
    return _key_handler.get(key_vk, lambda x: None)


_key_handler = {
    "Q": KeyHandler.handl_q
}
