import time

start_time = time.time()

def fact(num):
    numatstart = num
    i = num
    result = 1
    while i > 0:
            result = result * num
            num = num - 1
            i -= 1
    print(f"Factorial of {numatstart} is {result}")

fact(1000)

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed:", elapsed_time)