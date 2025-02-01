import re
import os

PATTERN = r'(mul|do|don\'t)\((?:(\d+)?,(\d+))?\)'

def solve(in_):
    line = in_.read()

    total = 0

    active = True
    matches = re.compile(PATTERN).finditer(line)
    for match in matches:
        op, a, b = match.groups()
        if op == 'do':
            active = True
        elif op == 'don\'t':
            active = False
        elif active:
            total += int(a)*int(b)

    print(total)

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), 'data', 'input.txt')) as i:
        solve(i)
