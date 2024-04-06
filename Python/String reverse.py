def reverse(string):
    i = 0
    j = len(string) - 1
    
    while i < j:
        key = string[i]
        string[i] = string[j]
        string[j] = key
        i += 1
        j -= 1
        
    string = "".join(string)
    print(string)

string = list(input("Enter a string: "))
reverse(string)