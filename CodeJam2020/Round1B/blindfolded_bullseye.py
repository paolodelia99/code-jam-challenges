import sys

t, a, b = map(int, input().split())

for case in range(1, t + 1):

    fail = False
    x, y = 0, 0

    for i in range(0, 300):
        print('{} {}'.format(x, y))
        sys.stdout.flush()

        response = input()
        if response == 'CENTER':
            break
        elif response == 'WRONG':
            fail = True
        elif response == 'MISS':
            print('do something')
        elif response == 'HIT':
            print('Do something else')

    if fail:
        sys.exit(1)
