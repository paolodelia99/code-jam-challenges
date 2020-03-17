from random import randint
import sys

t = int(input())

for _ in range(0,t):
    n,b,f = map(int, input().split())

    # Generate a casual sequence of n bits
    bits = []
    for i in range(0,n):
        bits.append(str(randint(0,1)))
    bits = "".join(bits)

    print(bits)
    sys.stdout.flush()
    dbResponse = input()
    for i in range(0,f):
        #Recalculte the bits
        print(bits)