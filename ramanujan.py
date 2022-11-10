"""Ramanujan's Formula for Pi
https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Sato_series
"""

import math


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1) 

def estimate_pi():
    k = 0
    fraction = 0
    constant = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        fraction += num / den
        inverse_of_pi = constant * num / den
        
        if abs(inverse_of_pi) < 1e-15:
            break
        k += 1

    return 1 / (constant * fraction) 

print(estimate_pi())
