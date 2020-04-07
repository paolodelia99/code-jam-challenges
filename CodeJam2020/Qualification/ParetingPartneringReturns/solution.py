t = int(input())

for case in range(1, t + 1):
    n = int(input())
    activities = []
    res = [None] * n

    for i in range(n):
        activities.append(list(map(int, input().split())) + [i])

    activities.sort()

    print(activities)

    # Store the end hours of the given activity assigned to C or J
    C = 0
    J = 0

    for s, e, i in activities:
        if s >= C:
            res[i] = 'C'
            C = e
        elif s >= J:
            res[i] = 'J'
            J = e

        if not all(res):
            ans = "IMPOSSIBLE"
        else:
            ans = ''.join(res)

    print('Case #{}: {}'.format(case, ans))
