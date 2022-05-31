from time import sleep
import time
import os


def timer_one_row():
    """
    Timer out

    """
    for i in range(5, 0, -1):
        print("\034.", end="")
        sleep(1)
    print('ok')


# timer_one_row()

def clearscreen(numlines=100):
    """Clear the console.
  numlines is an optional argument used only as a fall-back.
  """
    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums

    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


# import time


def check_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        # print(start)
        func(*args, **kwargs)
        end = time.time()
        # print(end)
        print("Time taken to execute function is ", end - start)

    return inner


@check_time
def task():
    # do something
    for i in range(100000000):
        pass


task()
