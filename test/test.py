import threading
import time
c=0
# 子執行緒的工作函數
def job(num):
  global c
  print("Thread", num)
  time.sleep(5)
  c+=2

# 建立 5 個子執行緒
threads = []
for i in range(83):
  threads.append(threading.Thread(target = job, args = (i,)))
  threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(83):
  threads[i].join()

print("Done.")
print(c)