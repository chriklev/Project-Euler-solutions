a = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i)

b = sum(a)
print(b)
