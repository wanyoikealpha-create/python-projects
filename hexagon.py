import turtle
def regular_polygon (t,n,side_length):
    angle=360/n
    
    for _ in range(n):
        t.forward(side_length) 
        t.left(angle)
    

t=turtle.Turtle()
regular_polygon(t,6,80)
turtle.done()