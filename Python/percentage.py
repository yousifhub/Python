def percentage(num,per):
    if per <= 100 and per >= 0:
        p = per / 100
        result = num * p
        print(f"{per}% of of {num} is {result}")
    else:
        print(f"Out of the 0-100% bounds")
        
while True:
    try:
        num = float(input("Enter number: "))
        percent = float(input("Enter percentage (without %): "))
        percentage(num,percent)
    except:
        print("Not a numerical value(s)")