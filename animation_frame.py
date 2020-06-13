# It uses time module.
import time

# func is the name of the function which has to be animated.
# delay is the time gap (in milliseconds) between any two successive recursion of the function func.
# *args object stores the arguments of func.
def animationFrame(func, delay, *args):
    time.sleep(delay / 1000)
    
    func(*args)
    
# Display some info about this module when run without importing.
if __name__ == "__main__":
    print("Written by Santanu Sikder.\n\nA small and simple module to run a function repeatedly with some time gap.")
