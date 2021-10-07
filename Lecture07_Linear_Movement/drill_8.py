import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    a = (y2 - y1)/(x2 - x1)
    b = y1 - x1 * a

    for x in range(x1, x2+1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

    pass


# 파라미터 방식
def draw_line(p1, p2, num):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    if num == 0:
        for i in range(-30, 30+1, 2):
            t = i / 2
            x = t - 2
            y = t ** 2 - 3
            draw_point((x, y))
    elif num == 1:
        for i in range(-30, 30+1, 2):
            t = i / 2
            x = t ** 2 - 3
            y = t - 2
            draw_point((x, y))
    elif num == 2:
        for i in range(-30, 30+1, 2):
            t = i / 2
            x = t - 2
            y = -(t ** 2 - 3)
            draw_point((x, y))
    elif num == 3:
        for i in range(-30, 30+1, 2):
            t = i / 2
            x = -(t ** 2 - 3)
            y = t - 2
            draw_point((x, y))
    pass


prepare_turtle_canvas()

p1 = -17, 222
p2 = 13, 222
draw_line(p1, p2, 0)

p1 = 15 ** 2 - 3, -15 - 2
p2 = 15 ** 2 - 3, 15 - 2
draw_line(p1, p2, 1)

p1 = -15 - 2, -(15 ** 2 - 3)
p2 = 15 - 2, -(15 ** 2 - 3)
draw_line(p1, p2, 2)

p1 = -(15 ** 2 - 3), -15 - 2
p2 = -(15 ** 2 - 3), 15 - 2
draw_line(p1, p2, 3)

turtle.done()