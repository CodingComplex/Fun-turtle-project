import turtle

clr = ['blue', 'green', 'white', 'red']
trt = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor('black')
trt.speed(10)
z = 0

for i in range(50):
    trt.forward(i*10)
    trt.right(144)
    trt.color(clr[z])
    if z == 3:
        z = 0
    else:
        z += 1
