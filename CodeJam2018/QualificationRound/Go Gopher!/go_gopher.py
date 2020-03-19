import sys


def deploy(A, i, j):
    lookup = set()
    while len(lookup) < 9:
        print(f'{i} {j}')
        sys.stdout.flush()
        ni, nj = map(int, input().split())
        if (ni, nj) == (-1, -1):  # error
            exit()
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


for case in range(int(input())):
    go_gohper()
