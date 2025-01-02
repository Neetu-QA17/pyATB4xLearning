# Time calculated while running a test case using custom decorator and wrrpaer function
import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by function {end_time - start_time}")
    return wrapper()

@time_decorator
def test_ui():
    time.sleep(2)
    print("Add a function, Time taken by this function")

@time_decorator
def test_ui2():
    time.sleep(5)
    print("Add a function, Time taken by this function")

# test_ui()

# Primary usage of decorator is to Before, After and Logging - adding logs to the automation