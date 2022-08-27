#TODO add tag windows (I create the script only for windows for the moment)
import concurrent.futures
import time, sys

def mainFunc():
    time.sleep(1)
    a = 1
    print(f"something {a}")
    return 0


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        e = executor.submit(mainFunc, 1)
