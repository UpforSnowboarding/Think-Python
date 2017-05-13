def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

first = b(2)
print(first)

second = a(2, 4)
print(second)

third = c(2, 3, 4)
print(third)
