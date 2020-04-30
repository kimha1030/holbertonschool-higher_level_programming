#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv) - 1
    sum_inf = 0
    if argc == 0:
        print("{:d}".format(argc))
    elif argc == 1:
        print("{:d}".format(argv[1]))
    else:
        for i in range(1, len(argv)):
            sum_inf = sum_inf + int(argv[i])
        print("{:d}".format(sum_inf))
