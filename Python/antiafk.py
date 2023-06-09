import pyautogui as gui
import random 
import time

while True:
    x = random.randint(50,1200)
    y = random.randint(50,600)
    print("Pos: X=",x,"Y=",y)
    gui.moveTo(x, y, 0.5)
    time.sleep(3)