import time
import random

def calling_function1():
    with open("flag.txt", "a") as f:
        f.write("a\n")

def calling_function2():
    with open("flag.txt", "a") as f:
        f.write("b\n")

def calling_function3():
    with open("flag.txt", "a") as f:
        f.write("c\n")

func_list = [calling_function1, calling_function2, calling_function3]

# while True:

random.choice(func_list)()