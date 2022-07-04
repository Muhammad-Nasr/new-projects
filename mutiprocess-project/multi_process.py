import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()

def do_something(seconds=1):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
    #results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)


## way 2 for multiprocessing
# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()  


## way 1 for multiprocessing

# p = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
# p.start()
# p2.start()
# p.join()
# p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')