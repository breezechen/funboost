# from funboost import boost_queue__fun_map
# # import test_consume
#
# import importlib
#
# importlib.import_module('test_frame/test_broker/test_consume.py'.replace('/','.')[:-3])
# print(boost_queue__fun_map)
#
# if __name__ == '__main__':
#
#     for queue_name,boost_fun in boost_queue__fun_map.items():
#         for i in range(100):
#             boost_fun.push(i,i*2)
#         boost_fun.consume()

import nb_log
import time

print(1)
for _ in range(1000000):
    time.time()

print(2)