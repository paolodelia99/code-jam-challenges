t = int(input())


def isSymmetric(mat):
    N = len(mat)
    for i in range(N):
        for j in range(N):
            if mat[i][j] != mat[j][i]:
                return False
    return True


for case in range(1, t + 1):
    r, c, h, v = map(int, input().split())
    h_space, v_space = h + 1, v + 1
    waffle = []
    c_row = [0]
    c_col = [0]
    res = ''

    for i in range(r):
        waffle.append(list(input()))
        c_row.append(waffle[i].count('@') + c_row[i])

    # remove first element
    c_row = c_row[1::]
    print(c_row)

    if sum(c_row) == 0:
        res = 'POSSIBLE'
    else:
        if c_row[len(c_row) - 1] % h_space == 0:

            a = c_row[len(c_row) - 1] // h_space
            initial_a = a

            for i in c_row:
                if a > c_row[len(c_row) - 1]:
                    print('2nd shot')
                    res = 'IMPOSSIBLE'
                    break

                print(f' {i} element a value {a}')

                if i == a:
                    a += initial_a

            if a == initial_a:
                res = 'IMPOSSIBLE'

            # check the columns
            if res != 'IMPOSSIBLE':

                # Transpose the matrix
                trans_waffle = rez = [[waffle[j][i] for j in range(len(waffle))] for i in range(len(waffle[0]))]
                print(trans_waffle)

                for i in range(len(trans_waffle)):
                    c_col.append(trans_waffle[i].count('@') + c_col[i])

                # remove first element
                c_col = c_col[1::]

                if c_col[len(c_col) - 1] % v_space == 0:

                    a = c_col[len(c_col) - 1] // v_space
                    initial_a = a

                    for i in c_col:
                        if a > c_col[len(c_col) - 1]:
                            print('3rd shot')
                            res = 'IMPOSSIBLE'
                            break

                        if i == a:
                            a += initial_a

                        print(f' {i} element a value {a}')

                    if a == initial_a:
                        res = 'IMPOSSIBLE'

                # Check symmetry
                if r == c:
                    if isSymmetric(waffle):
                        res = 'IMPOSSIBLE'
        else:
            print('first shot')
            res = 'IMPOSSIBLE'

    res = res if res == 'IMPOSSIBLE' else 'POSSIBLE'

    print("Case #{}: {}".format(case, res))
