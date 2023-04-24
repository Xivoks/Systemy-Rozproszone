import time
from pyRpc import PyRpc

def add(a, b):
    """ Returns a + b """
    return a + b

def subtract(a, b):
    """ Returns a - b """
    return a - b

def multiply(a, b):
    """ Returns a * b """
    return a * b

def divide(a, b):
    """ Returns a / b """
    return a / b

def favoriteColor():
    """ Tell you our favorite color """
    return "red"

myRpc = PyRpc("com.myCompany.MyApplication")
time.sleep(.1)

myRpc.publishService(add)
myRpc.publishService(subtract)
myRpc.publishService(multiply)
myRpc.publishService(divide)
myRpc.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    myRpc.stop()

