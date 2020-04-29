#!/usr/bin/python3
aux = 1
for i in range(122, 96, -1):
    if (aux == -1):
        May = (i - 32)
    else:
        May = i
    print("{:c}".format(May), end='')
    aux = -aux
