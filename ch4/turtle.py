import turtle
import math

bob = turtle.Turtle()

# Draw a square with bob

# 1)
def draw_square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# draw_square(bob)

# 2)

def draw_square_length(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

# draw_square_length(bob,50)

# 3)
def draw_polygon(t, l, n):
    sides = 360 / n
    for i in range(n):
        t.fd(l)
        t.lt(sides)

# draw_polygon(bob,50,15)

# 4)

def draw_circle(t, r):
    circum = 2 * math.pi * r
    n = 50
    l = circum / n
    draw_polygon(t,l,n)

draw_circle(bob,100)

# 5)

def polyline(t, n, l, angle):
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def polygon(t, n, l):
    angle = 360.0 / n
    polyline(t, n, l, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 10)


turtle.mainloop()


