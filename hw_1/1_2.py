import sys

def tail(filename=None, lines=10):
    if filename:
        with open(filename, 'r') as file:
            content = file.readlines()
    else:
        content = sys.stdin.readlines()
    for line in content[-lines:]:
        print(line, end='')

if __name__ == "__main__":
    filenames = sys.argv[1:]
    if filenames:
        for i, filename in enumerate(filenames):
            if len(filenames) > 1:
                print(f"==> {filename} <==")
            tail(filename, 10)
            if i < len(filenames) - 1:
                print()
    else:
        tail(lines=17)
