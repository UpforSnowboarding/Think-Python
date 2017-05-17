
def sqrt(a):
    epsilon = 0.00000000001
    x = 10
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            return y
            break
        x = y

sqrt(1)
import math


def test_square_root():
    print("a          mysqrt(a)          math.sqrt(a)          diff")
    print("-	      ---------	         ------------	       ----")
    for a in range(1, 10):
        print("%.1f       %.5f	             %.5f	               %f" % (a, sqrt(a), math.sqrt(a), sqrt(a) - math.sqrt(a)))


test_square_root()
