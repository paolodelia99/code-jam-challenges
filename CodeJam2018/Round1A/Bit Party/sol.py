t = int(input())


def check(t, r, b, m, s, p):
    c = [0] * len(m)

    for i in range(len(c)):
        c[i] = max(0, min(m[i], (t - p[i]) // s[i]))

    c.sort(reverse=True)

    return sum(c[:r]) >= b


def bit_party():
    r, b, c = map(int, input().split())
    m, s, p = [0] * c, [0] * c, [0] * c

    for i in range(c):
        m[i], s[i], p[i] = map(int, input().strip().split())

    left, right = 0, max(s) * b + max(p)

    while left <= right:
        mid = left + (right - left) // 2
        if check(mid, r, b, m, s, p):
            right = mid - 1
        else:
            left = mid + 1

    return left


for case in range(1, t + 1):
    print('Case #{}: {}'.format(case, bit_party()))
