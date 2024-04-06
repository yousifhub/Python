def fact(n):
    if n <= 1: return 1
    else: return n * fact(n - 1)
    
print("Factorial calculator")
num = float(input("Enter number: "))
print(f"factorial = {fact(num)}")