# import turtle
import turtle
from turtle import *
#screen for output

screen= turtle.Screen()

# Defining a turtle lInstance
t = turtle.Turtle()
t.penup()
t.goto(-350,450)
t.color("pink")
t.write("75th",font=("Verdana", 70,"normal"))
t.goto(-280,350)
t.color("red")
t.write("Happy Independence Day ",font=("Verdana", 10,"normal"))
t.goto(-280,280)
t.write("From Vipul Patil",font=("Verdana", 5,"normal"),move=True)

t.speed(2)
# initially penup ()
t.penup()
t.goto(-200, 125)
t.pendown()
# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right (90)
t.forward(400)
t.end_fill()
t.left (90)
t.forward (84)
#green color
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left (90)
t.forward(84)
t.end_fill ()
#Big Blue Circle
t.penup ()
t.goto (35, 0)
t.pendown()
t.color ("navy")
t.begin_fill()
t.circle (35)
t.end_fill()
# Big White Circle
t.penup ()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle (30)
t.end_fill()

t.penup ()
t.goto(-27,-4)
t.pendown()
t.color('navy')
for i in range (24):
	t.begin_fill()
	t.circle (2)
	t.speed(12)
	t.end_fill()
	t.penup()
	t.forward(7)
	t.right (15)
	t.pendown()
# Small Blue Circle
t.color('navy')
t.penup()
t.goto(10,0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
#The spokes of India Flag
t.penup()
t.goto(0,0)
t.speed(8)
t.pendown()
t.pensize(1)
for i in range (24):
	t.forward(30)
	t.backward(30)
	t.left(15)
#for stick of the flag
t.color ("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(180)
t.pendown()
t.speed(2)
t.forward (800)
