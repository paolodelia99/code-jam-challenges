import sys

t = int(input())


def is_area_complete_1(mat, x, y):
    isComplete = False

    for i in range(x_1-1, x + 1):
        for j in range(y_1-1, y + 1):
            if mat[i][j] == 'a':
                isComplete = True
            else:
                isComplete = False
                break
        if not isComplete:
            break

    if isComplete:
        if x + 2 > len(mat):
            return x, y + 1
        else:
            return x + 2, y
    else:
        return x, y


def is_area_complete_2(mat, x, y):
    isComplete = False

    for i in range(x_1 - 1, x + 1):
        for j in range(y_1 - 1, y + 1):
            if mat[i][j] == 'a':
                isComplete = True
            else:
                isComplete = False
                break
        if not isComplete:
            break

    if isComplete:
        if x + 2 > len(mat):
            return x, y + 2
        else:
            return x + 2, y
    else:
        return x, y


for _ in range(0, t):
    a = int(input())
    x,y = None,None

    if a == 20:
        x,y = 5,4
    else:
        x,y = 15,14

    x_1, y_1 = 1, 1

    mat = [['x' for x in range(x)] for y in range(y)]

    for i in range(0, 1000):
        print(f'{x_1 + 1} {y_1 + 1}')
        sys.stdout.flush()
        i_1, j_1 = map(int, input().split())
        if i_1 == j_1 == -1:
            break
        else:
            mat[i_1][j_1] = 'a'
            if a == 20:
                x_1, y_1 = is_area_complete_1(mat, x_1, y_1)
            else:
                x_1, y_1 = is_area_complete_2(mat, x_1, y_1)
