import time
import threading

print("Thess are the things that I've done so far...\n")


def brushMyTeeth(sleep):
    time.sleep(sleep)
    print("Brush my teeth")
    print(f"You've took {sleep} seconds to finish this task\n")


def shower(sleep):
    time.sleep(sleep)
    print("Took a shower")
    print(f"You've took {sleep} seconds to finish this task\n")


def eatMyBreakFast(sleep):
    time.sleep(sleep)
    print("Then i eat my breakfast")
    print(f"You've took {sleep} seconds to finish this task\n")


def drinkGreenTea(sleep):
    time.sleep(sleep)
    print("Finish drinking green tea")
    print(f"You've took {sleep} seconds to finish this task\n")


def study(sleep):
    time.sleep(sleep)
    print("Studied for 'four' hours")
    print(f"You've took {sleep} seconds to finish this task\n")


# we have dedicated each threads for each function
t1 = threading.Thread(target=brushMyTeeth, args=(1,))
t1.start()  # to start

t2 = threading.Thread(target=shower, args=(2,))
t2.start()

t3 = threading.Thread(target=eatMyBreakFast, args=(3,))
t3.start()

t4 = threading.Thread(target=drinkGreenTea, args=(4,))
t4.start()

t5 = threading.Thread(target=study, args=(5,))
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("end of todo-list")
# print(threading.activeCount())
# print(threading.enumerate())
print(time.perf_counter())

# import time
# import threading

# print("These are the things that I've done so far...\n")


# def brushMyTeeth(sleep, task_number):
#     time.sleep(sleep)
#     print(f"{task_number}. Brush my teeth")
#     print(f"You took {sleep} seconds to finish this task\n")


# def shower(sleep, task_number):
#     time.sleep(sleep)
#     print(f"{task_number}. Took a shower")
#     print(f"You took {sleep} seconds to finish this task\n")


# def eatMyBreakfast(sleep, task_number):
#     time.sleep(sleep)
#     print(f"{task_number}. Then I ate my breakfast")
#     print(f"You took {sleep} seconds to finish this task\n")


# def drinkGreenTea(sleep, task_number):
#     time.sleep(sleep)
#     print(f"{task_number}. Finished drinking green tea")
#     print(f"You took {sleep} seconds to finish this task\n")


# def study(sleep, task_number):
#     time.sleep(sleep)
#     print(f"{task_number}. Studied for 'four' hours")
#     print(f"You took {sleep} seconds to finish this task\n")


# tasks = [
#     (brushMyTeeth, 1),
#     (shower, 2),
#     (eatMyBreakfast, 3),
#     (drinkGreenTea, 4),
#     (study, 5),
# ]

# threads = []

# for task_number, (task, sleep) in enumerate(tasks, start=1):
#     thread = threading.Thread(target=task, args=(sleep, task_number))
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()

# print("End of todo-list")
