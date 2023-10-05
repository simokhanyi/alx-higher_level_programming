#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the command-line arguments excluding the script name
    arguments = sys.argv[1:]

    num_arg = len(arguments)

    print("Number of argument{}: ".format("s" if num_arg != 1 else ""), end="")
    if num_arg == 0:
        print(".", end="\n\n")
    else:
        print(":", end="\n\n")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))
