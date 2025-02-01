import re
import os


PATTERN = r'mul\((\d+),(\d+)\)'

def solve(in_):
    line = in_.read()

    total = 0
    matches = re.compile(PATTERN).finditer(line)
    for match in matches:
        a, b = map(int, match.groups())
        total += a*b

    print(total)

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), 'data', 'input.txt')) as i:
        solve(i)
