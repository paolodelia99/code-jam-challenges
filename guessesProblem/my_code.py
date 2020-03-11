t = int(input())

for i in range(0,t):
    exit = False
    a, b = input().split()
    n = int(input())
    #j is the current try
    for j in range(0,n):
        mid = (int(a)+int(b))//2
        print(mid)
        judgeResponse = input()
        if judgeResponse == "CORRECT":
            break
        elif judgeResponse == "TOO_BIG":
            b = mid
        elif judgeResponse == "TOO_SMALL":
            a = mid
        elif judgeResponse == "WRONG_ANSWER":
            exit = True
            break

    if exit:
        break
