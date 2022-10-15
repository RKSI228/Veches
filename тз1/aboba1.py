import threading
import time


def get_data(data):
    while True:
        
            thr_name="aa"
            print(f"[{threading.currentThread().name}-{data}")
            time.sleep(1)
            for i in range (1,True):
                print(f"current:{i}")
                time.sleep(1)
        



thr=threading.Thread(target=get_data, args=(str(time.time()),),name="thr=1")
thr.start()



