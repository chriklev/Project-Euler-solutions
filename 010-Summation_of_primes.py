s = 10
for x in range(7, 2000001, 2):
    for y in range(2, int((x / 2) + 1)):
        if x % y == 0:
            break
        elif y >= int(x / 2):
            s += x
    if x % 125 == 0:
        print(x)
print(s)
