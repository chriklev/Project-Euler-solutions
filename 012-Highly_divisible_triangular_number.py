#!/usr/bin/python3

from numba import jit
import time


@jit(nopython=True)
def find_that_numba():
    a = 1
    tri = 1
    while True:
        divisibles = 0
        for i in range(1, int(tri**0.5) + 1):
            if not tri % i:
                divisibles += 2
        if not tri**0.5 % 1:
            divisibles -= 1
        if divisibles > 500:
            print(tri)
            break
        a += 1
        tri += a


t0 = time.time()
find_that_numba()
print(time.time() - t0)
