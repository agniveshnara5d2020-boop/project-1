import turtle
spiral = turtle.Screen()
spiral.bgcolor('light blue')
spiral.title('Title')
my_pen = turtle.Turtle()
size = 0 
while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size = size - 5 
    size = size + 1 