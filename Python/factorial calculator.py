print("Factorial calculator")
num = int(input("Enter your number: "))
numatstart = num
i = num
result = 1
while i > 0:
        result = result * num
        num = num - 1
        i -= 1
print(f"Factorial of {numatstart} is {result}")