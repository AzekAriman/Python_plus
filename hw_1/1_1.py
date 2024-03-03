import sys
import fileinput

def print_numbered_lines():
    for i, line in enumerate(fileinput.input(), 1):
        print(f"{i}\t{line}", end='')

if __name__ == "__main__":
    print_numbered_lines()
