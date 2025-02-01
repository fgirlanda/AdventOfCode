import os


def solve(in_):
    lines = in_.readlines()

    safes = 0

    for line in lines:
        levels = list(map(int, line.split(' ')))

        if not is_safe(levels):
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i+1:]):
                    safes += 1
                    break
        else:
            safes += 1

    print(safes)

def is_safe(values):
    for l, r in zip(values, values[1:]):
        if values[0] < values[1] and not (1 <= r - l <= 3):
            return False
        if values[0] > values[1] and not (1 <= l - r <= 3):
            return False
        if l == r:
            return False

    return True

if __name__ == "__main__":
    with open(os.path.join(os.getcwd(), 'data', 'input.txt')) as i:
        solve(i)
