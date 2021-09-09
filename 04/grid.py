# Printing Grid

import turtle

startX = -250
startY = 250

turtle.penup()
turtle.goto(startX, startY)
turtle.pendown()

i = 0
while(i < 4):
      turtle.forward(500)
      turtle.right(90)
      i += 1

turtle.right(90)
i = 1
while(i < 5):
      turtle.goto(startX + 100 * i, startY)
      turtle.pendown()
      turtle.forward(500)
      turtle.penup()
      i += 1

turtle.goto(startX, startY - 100)

turtle.left(90)
i = 1
while(i < 5):
      turtle.goto(startX, startY - 100 * i)
      turtle.pendown()
      turtle.forward(500)
      turtle.penup()
      i += 1

turtle.exitonclick()
