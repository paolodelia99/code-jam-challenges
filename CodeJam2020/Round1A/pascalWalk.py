t = int(input())


def find_max_level(n: int):
    sums = [1]

    i = 1
    while max(sums) < n:
        sums.append(2 * sums[i - 1] + 1)
        i += 1

    return i


def create_binomial_matrix(level: int):
    mat = [[1 if j == i or j == 0 else 0 for j in range(0,level)] for i in range(0,level)]

    for i in range(0,len(mat)):
        for j in range(0, len(mat[i])):
            if j < i and j != 0:
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]

    return mat


for _ in range(1, t + 1):
    n = int(input())
    level = find_max_level(n)
    triangle = create_binomial_matrix(level)

    positions = [(1,1)]



