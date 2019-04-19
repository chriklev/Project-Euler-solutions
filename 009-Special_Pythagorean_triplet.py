#!/usr/bin/python3


def f():
    for a in range(500):
        for b in range(a + 1, 500):
            for c in range(b + 1, 500):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return(a * b * c)


print(f())
