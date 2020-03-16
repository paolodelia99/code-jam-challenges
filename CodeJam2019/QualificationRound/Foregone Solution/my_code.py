t = int(input())

for _ in range(1, t + 1):
    n = input()
    # reverse the string number
    n = ''.join(reversed(n))
    firstNum, secondNum = 0, 0

    for i in range(0,len(n)):
        # if n[i] is 4 I divide it into 2 and 2
        if n[i] == '4':
            firstNum += 2*10**i
            secondNum += 2*10**i
        else:
            firstNum += int(n[i])*10**i

    print("Case #{}: {} {}".format(_, firstNum, secondNum))
