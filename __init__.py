import random


def plus(num1, num2):
    return num1 + num2


def get_random():
    num1 = random.randint(0, 100)
    num2 = num1 + 50
    num3 = plus(num1, num2)
    print(num3)


get_random()
