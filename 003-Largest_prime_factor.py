a = 600851475143
pf = [a]
i = 2
while i < pf[pf.count("") - 1]:
    if pf[pf.count("") - 1] % i == 0:
        pf.append(i)
        pf.append(int(pf.pop(pf.count("") - 2) / i))
    i = i + 1
pf.sort()
print(pf)
