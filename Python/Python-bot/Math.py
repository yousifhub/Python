from random import randint

def tobinary(txt):
    l,m=[],[]
    for i in txt:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

def rint(num1, num2):
    value = randint(num1, num2)
    return value

def fact(num):
    i = int(num)
    result = 1
    while i > 0:
        result = result * i
        i -= 1
    return result

def oddoreven(num):
    x = int(num)
    if x % 2 == 0: return (f"{num} is an Even number.")
    else: return (f"{num} is an Odd number.")
    
def remainder(num1, num2):
    i = int(num1) % int(num2)
    return (f"{num1} % {num2} = {i}")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)