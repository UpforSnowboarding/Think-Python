import turtle

bob = turtle.Turtle()
bob.color("blue")

def draw_koch(t, length):

    if length < 10:
        t.fd(length)
        return
    angle1 = 60
    angle2 = 120
    n = length / 3
    draw_koch(t,n)
    t.lt(angle1)
    draw_koch(t,n)
    t.rt(angle2)
    draw_koch(t,n)
    t.lt(angle1)
    draw_koch(t, n)

def draw_snow_flake(t, n):
    for i in range(3):
        draw_koch(t,n)
        t.rt(120)

bob.pu()
bob.goto(-150, 90)
bob.pd()
draw_snow_flake(bob,300)
turtle.mainloop()
