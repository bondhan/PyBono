import threading,queue
import time
from pprint import pprint


def calc_square(length):
    time.sleep(0.2)
    return length * length


def calc_cube(length):
    time.sleep(0.2)
    return length * length * length


def do_calc(q):
    global result_squares
    global result_cubes
    while True:
        number = q.get()
        result_squares[f'{number}'] =  calc_square(number)
        result_cubes[f'{number}'] = calc_cube(number)
        q.task_done()

if __name__ == '__main__':
    num_thread = 25
    q = queue.Queue()
    start = time.time()
    result_squares = {}
    result_cubes = {}

    for i in range(num_thread):
        t = threading.Thread(target=do_calc, args=(q,))
        t.setDaemon(True)
        t.start()

    for i in range(1, 21, 1):
        print(f"putting {i}")
        q.put(i)

    print ('Main thread waiting')
    q.join()
    print (f'Done in {(time.time() - start)} seconds')

    s = [(k, result_squares[k]) for k in sorted(result_squares, key=result_squares.get, reverse=False)]
    c = [(k, result_cubes[k]) for k in sorted(result_cubes, key=result_cubes.get, reverse=False)]

    pprint(s)
    pprint(c)
