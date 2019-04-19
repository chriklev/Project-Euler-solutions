#!/usr/bin/python3

a = [1, 2]
b = 0
while a[a.count("") - 1] < 4000000:
    a.append(a[a.count("") - 1] + a[a.count("") - 2])
for i in a:
    if i % 2 == 0:
        b = b + i
print(b)
