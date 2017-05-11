def is_triangle(a, b, c):
    if a + b < c:
        print("Cannot form triangle")
    elif a + c < b:
        print("Cannot form triangle")
    elif c + b < a:
        print("Cannot form triangle")
    else:
        print("Yay, we can form a triangle")


def is_triangle_input():
    a = int(input("Please enter a number for a: "))
    b = int(input("Please enter a number for b: "))
    c = int(input("Please enter a number for c: "))
    is_triangle(a,b,c)

is_triangle(4, 10, 3)
is_triangle_input()
