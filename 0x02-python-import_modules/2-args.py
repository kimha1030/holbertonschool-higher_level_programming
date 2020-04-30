#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
