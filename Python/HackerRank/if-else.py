num = int(input("Enter a number: "))
n = num % 2
print("n = ",n)
print("num = ",num)
if n == 0:
    if num >=2 and num <=5:
        print("Not Weird")
    elif num >=6 and num <=20:
        print("Weird")
    else: 
        print("Not Weird")
else: 
    print("Weird")