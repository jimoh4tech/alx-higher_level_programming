#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    len = len(sys.argv)
    if len - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    op = sys.argv[2]

    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
