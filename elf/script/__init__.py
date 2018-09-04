from .牛头 import 二连


class KeyHandler(object):
    w_down = False

    @classmethod
    def handl_w(cls, is_down):
        cls.w_down = is_down

    @classmethod
    def handle_key_down(cls):
        if cls.w_down:
            二连.execution()


def get_key_handler(key_vk):
    return _key_handler.get(key_vk, lambda x: None)


_key_handler = {
    "W": KeyHandler.handl_w,
}


# from .攻击 import 攻击
# from .状态 import 状态


# class KeyHandler(object):
#     q_down = False
#     r_down = False

#     @classmethod
#     def handl_q(cls, is_down):
#         cls.q_down = is_down

#     @classmethod
#     def handl_r(cls, is_down):
#         cls.r_down = is_down

#     @classmethod
#     def handle_key_down(cls):
#         if cls.q_down:
#             攻击.execution()
#         if cls.r_down:
#             状态.execution()


# def get_key_handler(key_vk):
#     return _key_handler.get(key_vk, lambda x: None)


# _key_handler = {
#     "Q": KeyHandler.handl_q,
#     "R": KeyHandler.handl_r
# }
