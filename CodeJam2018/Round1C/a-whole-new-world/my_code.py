import collections
import functools


def dfs(trie, lookup, i, curr):
    if i == len(lookup):
        return "-"
    if len(trie) != len(lookup[i]):
        for c in lookup[i]:
            if c in trie:
                continue
            # generate unique word
            curr.append(c)
            nodes = trie.values()[0]
            while nodes:
                c = nodes.keys()[0]
                curr.append(c)
                nodes = nodes[c]
            break
        return "".join(curr)
    for c in trie:
        curr.append(c)
        result = dfs(trie[c], lookup, i + 1, curr)
        curr.pop()
        if result != "-":
            return result
    return "-"


def a_whole_new_word():
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    N, L = map(int, input().strip().split())
    lookup = [set() for _ in range(L)]
    for _ in range(N):
        word = input().strip()
        for i in range(L):
            lookup[i].add(word[i])
        functools.reduce(dict.__getitem__, word, trie)
    return dfs(trie, lookup, 0, [])


for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, a_whole_new_word()))
