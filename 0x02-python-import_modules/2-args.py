#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if (num == 1):
        print("{} argument:".format(num))
    elif num > 1:
        print("{} arguments:".format(num))
    else:
        print("0 arguments.")
        for n in range(num):
            print("{}: {}".format(n + 1, argv[n + 1]))
