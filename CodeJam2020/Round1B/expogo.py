def expogo():
    x, y = map(int, input().split())

    # if (abs(x) + abs(y))%2 == 0 it turns out to be impossible
    if (abs(x) + abs(y)) % 2 == 0:
        return 'IMPOSSIBLE'

    # find the maximum pow of 2
    n, total = 0, 0
    while not (total >= abs(x) + abs(y)):
        n = 1 if not n else n * 2
        total += n

    result = []

    while n:
        if abs(x) > abs(y):
            if x > 0:
                result.append('E')
                x -= n
            else:
                result.append('W')
                x += n
        else:
            if y > 0:
                result.append('N')
                y -= n
            else:
                result.append('S')
                y += n

        n //= 2

    return "".join(reversed(result))


for case in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(case, expogo()))
