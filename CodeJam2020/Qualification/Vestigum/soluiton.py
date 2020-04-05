for case in range(1,int(input())+1):
    n = int(input())
    matrix = []
    trace = 0
    rep_row, rep_col = 0, 0

    for _ in range(n):
        matrix.append((list(map(int, input().split()))))

    # compute the trace
    for i in range(len(matrix)):
        trace += matrix[i][i]

    # count rep rows
    for i in range(len(matrix)):
        count_dict = {x:matrix[i].count(x) for x in matrix[i]}
        print(count_dict)
        for num in count_dict.values():
            if num != 1:
                rep_row += 1
                break

    #transpose
    matrix = rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # count rep cols
    for i in range(len(matrix)):
        count_dict = {x: matrix[i].count(x) for x in matrix[i]}
        print(count_dict)
        for num in count_dict.values():
            if num != 1:
                rep_col += 1
                break

    print('Case #{}: {} {} {}'.format(case,trace,rep_row,rep_col))