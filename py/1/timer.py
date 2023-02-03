import time
def procedure():
    time.sleep(2.5)

# time.clock
t0 = time.perf_counter()
# print('計時開始:')
procedure()
print (time.perf_counter() - t0)

# time.time
t0 = time.time()
procedure()                    #這裡呼叫副程式暫停2.5秒
print (time.time() - t0)

