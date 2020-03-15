from random import randint
import re

t = int(input())

for _ in range(1,t+1):
    n = int(input())
    repeatCicle = True
    firstNumber, randnum = 0,0

    while repeatCicle:
        randnum = randint(1,n/2)
        firstNumber = n - randnum
        randnum_check = re.match(r"*4*", str(randnum))
        repeatCicle = True if '4' in str(randnum) and '4' in str(firstNumber) else False


    print("Case #{}: {} {}".format(_, firstNumber,randnum))