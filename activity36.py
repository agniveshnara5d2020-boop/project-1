import turtle 
my = turtle.Screen()
my.bgcolor('light pink')
my.title('Triangle Spiral')
my_pen = turtle.Turtle()
my_pen.speed(0)

size = 0 
while True:
    for i in range(3):
        my_pen.fd(size+1)
        my_pen.left(120)
        size = size - 5
    size = size + 1