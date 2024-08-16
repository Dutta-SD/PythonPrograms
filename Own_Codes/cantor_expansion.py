# TO display the cantor expansion of a number n
from math import factorial


def cantorExpansion(a):
    if a == 0:
        return [0]

    x = 0
    while factorial(x) <= a:
        x += 1

    c = []
    f = factorial(x)

    while x != 0:
        c_temp = a // f
        a = a - (c_temp * f)
        f //= x
        x -= 1
        c.append(c_temp)
    return c[1:]


for i in range(100):
    print(f"Cantor Expansion of {i} is {''.join(map(str, cantorExpansion(i)))}")
