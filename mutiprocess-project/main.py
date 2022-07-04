import concurrent.futures
import time
import threading

start = time.perf_counter()


def do_something(seconds=1):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    
    return f'Done Sleeping...{seconds}'

secs = [1, 2, 3, 4, 5]
for sec in secs:
    print(do_something(sec))

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [1, 2, 3, 4, 5]
#     results = executor.map(do_something, secs)

#     for result in results:
#         print(result)

#threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')