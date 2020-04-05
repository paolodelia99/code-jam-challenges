from random import randint
import sys

for _ in range(int(input())):
    b = input()
    n = len(b)
    bit_array = list(b)
    isEqual = False

    for i in range(0, 150):
        if i % 10 == 0:
            position = randint(1, n + 1)
            print(str(position))
            sys.stdout.flush()
            # Check if the array has no changament
            bit = input()
            if b[position] == bit:
                print("".join(bit_array))
                if input() == 'N':
                    break
            else:
                isEqual = False
        else:
            if not isEqual:
                position = 1
                print(position)
                sys.stdout.flush()
                bit = input()
                bit_array[position - 1] = bit
                position += 1
