t = int(input())

for case in range(1,t+1):
    r,b,c = map(int, input().split())
    cashier = []

    for i in range(c):
        cashier.append(tuple(map(int, input().split())))


    max_bit = b / r if b % r == 0 else (b % r) + 1

    time_for_cash = []

    for i in cashier:
        if i[0] >= max_bit:
            time_for_cash.append((max_bit * i[1]) + i[2])
