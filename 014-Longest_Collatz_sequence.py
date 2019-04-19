#!/usr/bin/python3


def find_length(val, length=0):
    length += 1
    if val == 1:
        return(length)
    elif not val % 2:
        return(find_length(val//2, length=length))
    else:
        return(find_length(3*val+1, length=length))


largest = 0
longest = 0
for i in range(1, int(1e6)):
    n = find_length(i, length=0)
    if n > largest:
        largest = n
        longest = i

print(longest)
