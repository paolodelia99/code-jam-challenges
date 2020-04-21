import sys


def binary_search(left, right, check, is_left):
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid) == is_left:
            right = mid - 1
        else:
            left = mid + 1
    return left if is_left else right


def query(x, y):
    print('{} {}'.format(x, y))
    sys.stdout.flush()
    r = input().strip()
    if r == "WRONG":  # error
        exit()
    if r == "CENTER":
        raise
    return r == "HIT"


def blindfolded_bullseye():
    for x0, y0 in [(-a, 0), (a, 0), (0, -a), (0, a)]:
        if query(x0, y0):  # at most 4 queries, which cover all possible centers of 3 test cases
            break
    left_x = binary_search(-M, x0, lambda x: query(x, y0), True)
    right_x = binary_search(x0, M, lambda x: query(x, y0), False)
    left_y = binary_search(-M, y0, lambda y: query(x0, y), True)
    right_y = binary_search(y0, M, lambda y: query(x0, y), False)
    query((left_x + right_x) // 2, (left_y + right_y) // 2)
    exit()  # should not reach here


M = 10 ** 9 # Since we are in nm

t, a, b = map(int, input().split())

for case in range(t):
    try:
        blindfolded_bullseye()
    except:
        pass
