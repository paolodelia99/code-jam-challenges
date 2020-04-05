for case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    res = ''

    if float(k/n).is_integer() and 1 <= k / n <= n:
        res = 'POSSIBLE'
        matrix = [[0 for i in range(n)] for j in range(n)]
        num = k // n

        for i in range(0, len(matrix)):
            if i == 0:
                matrix[i][i] = num
                for j in range(1, len(matrix)):
                    num = num + 1 if num + 1 <= n else 1
                    matrix[i][j] = num
            else:
                matrix[i] = matrix[i - 1][-1:] + matrix[i - 1][:-1]

        print('Case #{}: {}'.format(case, res))
        for i in range(0, len(matrix)):
            print(*matrix[i])
    else:
        res = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(case, res))
