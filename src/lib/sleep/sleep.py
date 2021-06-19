from time import time, sleep

_start = time()

def _sleep(time_len: float):

    sleep(time_len - ( (time() - _start) % time_len ))
    
    return 1