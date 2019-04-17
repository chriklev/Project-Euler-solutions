l = list()

def revint(a):
    st = ""
    f = list()
    f.extend(str(a))
    f.reverse()
    for i in f:
        st += i
    return(int(st))

for a in range(100, 999):
    for b in range(100, 999):
        if a * b == revint(a * b):
            l.append(a * b)
l.sort()
print(l)
