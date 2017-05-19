import math

def factorial(n):
    """Uses recursion to compute the value of factorial(n)
    4! = 4 * 3 * 2 * 1 = 
    """

    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

print(factorial(4))

def estimate_pi():
    """Computes the estimate of pi
    compare result to math.pi"""

    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:

        numer = factorial(4 * k) * (1103 + 26390 * k)
        denom = factorial(k)**4 * 396**(4*k)
        eqn = factor * (numer / denom)
        total += eqn

        if abs(eqn) <  1e-15:
            break
        k += 1

    return 1 / total

pi_est = estimate_pi()
print(pi_est)
print(math.pi)

delta = pi_est - math.pi
print(delta)
