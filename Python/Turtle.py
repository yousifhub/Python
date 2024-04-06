import turtle

def square():
    length = int(input("Enter line length: "))
    color = input("Enter the color: ")
    turtle.color("black", color)
    turtle.speed(1)
    turtle.begin_fill()
    turtle.fd((length))
    turtle.rt(90)
    turtle.fd((length))
    turtle.rt(90)
    turtle.fd((length))
    turtle.rt(90)
    turtle.fd((length))
    turtle.end_fill()
    
def circle():
    radius = int(input("Enter the radius: "))
    color = input("Enter the color: ")
    turtle.color("black", color)
    turtle.speed(1)
    turtle.begin_fill()
    turtle.circle((radius))
    turtle.end_fill()
    
def triangle():
    length = int(input("Enter line length: "))
    color = input("Enter the color: ")
    turtle.color("black", color)
    turtle.speed(1)
    turtle.begin_fill()
    turtle.fd((length))
    turtle.lt(120)
    turtle.fd((length))
    turtle.lt(120)
    turtle.fd((length))
    turtle.end_fill()
    
def dot():
    size = int(input("Enter the size: "))
    color = input("Enter the color: ")
    turtle.color(color)
    turtle.speed(1)
    turtle.dot((size))
    
print("1: Square")
print("2: Circle")
print("3: Triangle")
print("4: Dot")
selection = int(input("Enter the number of the shape: "))
turtle.screensize(3840, 2160)
turtle.hideturtle()

if selection == 1: square()
elif selection == 2: circle()
elif selection == 3: triangle()
elif selection == 4: dot()
else: print("Not a selection")

turtle.exitonclick()