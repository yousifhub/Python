import matplotlib.pyplot as plt
import numpy as np

title = input("Enter the pie title: ")
numval = int(input("Enter the number of values: "))
numbers = []
    
for i in range(numval):
    value = float(input("Enter value number {}: ".format(i+1)))
    numbers.append(value)

result = np.array(numbers)

plt.pie(result)
plt.title(title)

if numval == 0:
    plt.title("There is nothing to show!")
    
plt.show()