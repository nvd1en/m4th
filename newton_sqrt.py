"""Newton's Method
https://en.wikipedia.org/wiki/Newton%27s_method
"""
def sqrt(n):
    x = n / 2
    while True:
        square_root = (x + n/x) / 2
        if abs(square_root - x) < 1e-15:
            break
        x = square_root
    return square_root
