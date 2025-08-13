import turtle
t=turtle.Turtle()
t.speed(0)
n=int(input("Enter the number of petals:"))
for i in range(n):
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)
    t.left(360/n)
t.hideturtle()
turtle.done()
