def patternMatching():
    n = int(input())
    p = [input().strip().split('*') for _ in range(n)]

    prefix, suffix = "", ""

    # Find the longest prefix and suffix
    for i in range(n):
        if len(prefix) < len(p[i][0]):
            prefix = p[i][0]
        if len(suffix) < len(p[i][-1]):
            suffix = p[i][-1]

    # if the prefix or the suffix don't contain
    # all the prefix return *
    for i in range(n):
        if not prefix.startswith(p[i][0]):
            return '*'
        if not suffix.endswith(p[i][-1]):
            return '*'

    result = [prefix]

    # add to the prefix all the strings that aren't
    # suffix or prefix
    for i in range(n):
        result.extend(p[i][1:-1])

    result.append(suffix)

    return "".join(result)


for case in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(case, patternMatching()))
