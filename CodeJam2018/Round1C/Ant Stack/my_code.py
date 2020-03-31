t = int(input())


def countAnts(ants, x, y):
    if x >= len(ants):
        return 0
    else:
        if ants[x]*6 >= y:
            return 1 + countAnts(ants, x + 1, y+ants[x])
        else:
            return countAnts(ants, x + 1 , y)


for case in range(1, t + 1):
    n = int(input())
    ants = list(map(int, input().split()))

    res = countAnts(ants , 0 , 0)

    print("Case #{}: {}".format(case, res))
