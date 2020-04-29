#!/usr/bin/python3
aux = 1
for i in range(122, 96, -1):
    if (aux == -1):
        m = i - 32
    else:
        m = i
    print("{:c}".format(i), end='')
    aux = -aux
