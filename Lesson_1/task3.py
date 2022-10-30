import time
time.time()
print("unix time:")
print(time.time())
print ('-' * 20)
print("convenient unix time:")
timeline = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
print(timeline) 