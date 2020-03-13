t = int(input())


def computeMinSwap(p, d, damage):
    swaps = 0
    while damage > d:
        # find the lastest CS index in p
        i = p.rfind('CS')
        # If it doesn't exists and damage > d IMPOSSIBLE
        if i == -1:
            swaps = 'IMPOSSIBLE'
            break
        p_list = list(p)
        p_list[i], p_list[i + 1] = p_list[i + 1], p_list[i]
        p = "".join(p_list)
        swaps += 1
        damage = computeDamage(p)

    return swaps


# Get the damage from the p string
def computeDamage(p):
    damage, damage_per_shoot = 0, 1
    for i in range(len(p)):
        if p[i] == 'S':
            damage += damage_per_shoot
        else:
            damage_per_shoot *= 2

    return damage


for _ in range(1, t + 1):
    d, p = map(str, input().split())
    d = int(d)
    res = None

    if 'S' not in p:
        res = 0
    elif p.count('S') > d:
        res = 'IMPOSSIBLE'
    else:
        damage = computeDamage(p)

        if damage <= d:
            res = 0
        else:
            res = computeMinSwap(p, d, damage)

    print("Case #{}: {}".format(_, res))
