import multiprocessing
import time


def cube(value):
    # time.sleep(sleep)
    print("Cube :".format(value * value * value))
    # print(f"It took {sleep} seconds to finish this program")


def square(value):
    # time.sleep(sleep)
    print("Square :".format(value * value))
    # print(f"It took {sleep} seconds to finish this program")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=cube, args=(10,))
    p2 = multiprocessing.Process(target=square, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")
