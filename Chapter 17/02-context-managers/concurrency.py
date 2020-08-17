#%% Verbose lock acquiring and releasing can be dangerous when errors occur.
import threading

my_lock = threading.Lock()

try:
    my_lock.acquire()
    with open('02-context-managers/sample1.txt', 'r') as f:
        lines = f.readlines()
        print(lines)
    my_lock.release()
except:
    print('Some problem occurred.')

my_lock.acquire()
print('Lock acquired')

#%% Locks can be safely acquired and released using a context manager.
import threading

my_lock = threading.Lock()

try:
    with my_lock:
        with open('02-context-managers/sample1.txt', 'r') as f:
            lines = f.readlines()
except:
    print('Some problem occurred.')

my_lock.acquire()
print('Lock acquired.')

#%% The same logic applies for a pool of processes.
import multiprocessing

with multiprocessing.Pool(4) as pool:
    pool.map(print, [f'Hello {i}' for i in range(10)])
