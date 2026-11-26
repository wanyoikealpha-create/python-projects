import turtle
t=turtle.Turtle()
t.speed(0)

radius=80
petals=12
angle=360/petals

for _ in range (petals):
    t.circle(radius)
    t.left(angle)