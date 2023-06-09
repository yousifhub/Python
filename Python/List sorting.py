numval = int(input("Enter the amount of numbers you want sorted: "))
numbers = []

for i in range(numval):
    value = input("Enter number at index {}: ".format(i+1))
    numbers.append(value)

print("1: Normal")
print("2: Reversed")
x = int(input("Sort type: "))

if x == 1:
    numbers.sort()
elif x == 2:
    numbers.sort(reverse=True)

print("Sorted list: ")
for i in numbers:
    print(i, end=" ")