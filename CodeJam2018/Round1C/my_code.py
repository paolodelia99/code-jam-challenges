from functools import reduce
from random import randint

t = int(input())


def create_new_word(sets, size, l):
    letters = []

    for i in range(l):
        letters.append(sets[i][randint(0, size)])

    letters = "".join(letters)
    return letters


for case in range(1, t + 1):
    n, l = map(int, input().split())
    words = []
    sets_lists = [set() for _ in range(l)]

    for k in range(n):
        words.append(input())
        for i in range(l):
            sets_lists[i].add(words[k][i])

    res = ""
    if l == 1:
        res = "-"
    else:
        sets_size = [len(i) for i in sets_lists]
        combinantion = reduce((lambda x, y: x * y), sets_size)
        if combinantion == n:
            res = '-'
        else:
            res = create_new_word(sets_lists,sets_size, l)
            while res in words:
                res = create_new_word(sets_lists,sets_size, l)

    print('Case #{}: {}'.format(case, res))
