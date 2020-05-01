#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = (len(argv) - 1)
    if (argc == 3):
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if ((op != '+') and (op != '-') and (op != '*') and (op != '/')):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if (op == '+'):
                print("{} {} {} = {}".format(a, op, b, add(a, b)))
            elif (op == '-'):
                print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            elif (op == '*'):
                print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
