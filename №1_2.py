import time
import msvcrt
time_limit = int(input())

start_time = time.time()

while (time.time() - start_time) < time_limit:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time)
    time.sleep(1)

    if msvcrt.kbhit():
        break
