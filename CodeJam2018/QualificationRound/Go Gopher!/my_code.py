import sys

t = int(input())


def is_area_complete_1(mat, x, y):
    is_complete = True
    for i in range(x-1, x + 2):
        for j in range(y-1, y + 2):
            if mat[i][j] != 'a':
                is_complete = False
                break
        if not is_complete:
            break

    if is_complete:
        if y + 2 > len(mat[0])-1:
            return x + 1, 1
        else:
            return x, y + 2
    else:
        return x, y


def is_area_complete_2(mat, x, y):
    is_complete = False

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if mat[i][j] != 'a':
                is_complete = False
        if not is_complete:
            break

    if is_complete:
        if y + 2 > len(mat[0]):
            return x +2, 1
        else:
            return x, y + 2
    else:
        return x, y


for _ in range(0, t):
    a = int(input())
    x,y = None,None
    error = False

    if a == 20:
        x,y = 4,5
    else:
        x,y = 14,15

    x_1, y_1 = 1, 1

    mat = [['x' for y in range(y)] for x in range(x)]

    for i in range(0, 1000):
        print(f'{x_1 + 1} {y_1 + 1}')
        sys.stdout.flush()
        i_1, j_1 = map(int, input().split())
        if (i_1 == j_1 == -1) or i == 999:
            error = True
            break
        elif i_1 == j_1 == 0:
            break
        else:
            mat[i_1-1][j_1-1] = 'a'

            # print the matrix
            # for i in range(0, len(mat)):
            #     print(mat[i])

            if a == 20:
                x_1, y_1 = is_area_complete_1(mat, x_1, y_1)
            else:
                x_1, y_1 = is_area_complete_2(mat, x_1, y_1)

    if error:
        break