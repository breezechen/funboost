

import os
import threading

for _ in range(8):
    threading.Thread(target=os.system,args=('python test_rabbitmq_consume.py',)).start()