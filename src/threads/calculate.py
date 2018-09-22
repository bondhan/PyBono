import threading
import time


def calc_square(length):
        time.sleep(0.2)
        print(f"square {length} = {length * length}")

def calc_cube(length):
        time.sleep(0.2)
        print(f"cube {length} = {length * length * length}")


if __name__ == '__main__':
    threadList = []

    # start = time.time()
    # for l in range(20):
    #     calc_square(l)
    #     calc_cube(l)
    #
    # print(f"Done in {(time.time() - start)} seconds")

    start = time.time()
    for l in range(20):
        t1 = threading.Thread(target=calc_square, args=(l,))
        t1.start()
        t2 = threading.Thread(target=calc_cube, args=(l,))
        t2.start()

        threadList.append(t1)
        threadList.append(t2)

    for t in threadList:
        t.join()

    print(f"\nThread Count: {threads.active_count()}")

    print(f"Done in {(time.time() - start)} seconds")