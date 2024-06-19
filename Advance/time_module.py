import time

# print(time.time())
# # Getting epoch
print(time.gmtime(0))

# Getting current time in seconds since epoch
curr = time.time()
print("Current time in seconds since epoch :", curr)

# time in seconds since the epoch to a string in local time.
print("Current second :", time.time())

# Getting time string from seconds
curr = time.ctime(1718381758.8426838)
print("Current time :", curr)

# Getting current time
local_time = time.localtime()
time = time.asctime(local_time)
print("Current time", time)

# Delaying Execution of Programs
for i in range(
    10, 0, -1
):  # Start at 10, stop at 1 (exclusive), step by -1 to go in reverse
    time.sleep(2)  # sec as parameter
    print(i, "", end="", flush=True)  # Force the output to be flushed immediately

# time.strftime() method
current_time = time.gmtime()
local_time = time.strftime(
    "%a, %d %b %Y %H:%M:%S %I %p", current_time
)  # %I for 12h and %p for AM or PM
print(local_time)
