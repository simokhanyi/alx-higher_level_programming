#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s):", num_args)
        print(":")
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
