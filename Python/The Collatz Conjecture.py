import matplotlib.pyplot as plt
from tkinter import *

# The Collatz Conjecture Part
def Collatz(event = None):
    num = int(txt.get())
    numstart = num

    val = []
    iter = []
    
    i = 0
    while num > 1:
        val.append(num)
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        
        i += 1    
        iter.append(i)
        
    plt.title(f"The Collatz Conjecture of {numstart}, Peaked at {max(val)} and ended at {max(iter)} steps")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.plot(iter, val)
    plt.show()

# GUI Part
def app():
    global txt
    
    root = Tk()
    root.title("The Collatz Conjecture")
    
    lbl = Label(root, text = "Enter Number")
    lbl.pack()
    
    txt = Entry(root)
    txt.pack()
    txt.bind("<Return>", Collatz)
    
    btn = Button(root, text="Done", command=Collatz)
    btn.pack()
    
    root.mainloop()
    
app()