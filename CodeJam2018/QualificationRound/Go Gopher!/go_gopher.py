import sys

t = int(input())


def deploy(A, i, j):
    lookup = set()
    while len(lookup) < 9:
        print(f'{i} {j}',file=sys.stderr)
        sys.stdout.flush()
        ni, nj = map(int, input().split())
        if (ni, nj) == (-1, -1):  # error
            sys.exit(0)
        if (ni, nj) == (0, 0):  # done
            return True
        lookup.add((ni - i + 1) * 3 + (nj - j + 1))
    return False


def go_gohper():
    A = int(input())
    i = 2
    while True:
        if deploy(A, i, 2):
            break
        A -= 9
        i += 3


for case in range(0, t):
    go_gohper()
