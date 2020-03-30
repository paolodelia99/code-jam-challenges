t = int(input())


def countAnts(ants, x, y):
    if x == 0:
        return 1
    else:
        print(ants[0:x])
        print(sum(ants[0:x]))
        print(sum(ants[0:x]) < y)
        if sum(ants[0:x]) <= y:
            return 1 + countAnts(ants, x - 1, min(ants[x-1] * 6, y-ants[x]))
        else:
            return countAnts(ants, x - 1, y)


for case in range(1, t + 1):
    n = int(input())
    ants = list(map(int, input().split()))

    res = countAnts(ants , len(ants)-1 , ants[len(ants)-1]*6)

    print("Case #{}: {}".format(case, res))
