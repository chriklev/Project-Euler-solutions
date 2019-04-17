def d():
    i = 1
    while True:
        for x in range(2, 21):
            if i % x == 0:
                if x == 20:
                    return(i)
            else:
                i += 1
                break
        if i % 100000 == 0:
            print(i)
print(d())
