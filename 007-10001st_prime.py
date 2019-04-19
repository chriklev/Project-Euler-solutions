#!/usr/bin/python3

i = 2
a = 2
while a <= 10001:
    i += 1
    for b in range(2, i):
        if i % b == 0:
            break
        elif b == i - 1:
            a += 1
    if i % 1000 == 0:
        print(i)
print(i)
