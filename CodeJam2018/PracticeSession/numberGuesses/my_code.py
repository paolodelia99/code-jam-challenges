import sys


# Do the binary Search
def solve(a, b):
    mid = (a + b) // 2
    print(mid)
    sys.stdout.flush()
    judgeResponse = input()
    if judgeResponse == "CORRECT":
        return
    elif judgeResponse == "TOO_SMALL":
        a = mid + 1
    else:
        b = mid - 1
    solve(a, b)


# Get the numbers of tests
T = int(input())
for _ in range(T):
    #Get the range
    a, b = map(int, input().split())
    # Get the numer of inputs
    _ = int(input())
    solve(a + 1, b)
