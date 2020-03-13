from string import ascii_uppercase

t = int(input())

for _ in range(1,t+1):
    no_parties = int(input())
    parties = list(map(int, input().split()))
    output = []

    while sum(parties) > 0:
        # get the index of the remaining parties
        remaining = [i for i in range(no_parties) if parties[i] > 0]
        # Get the party with the max size
        size_of_largest = max(parties)
        if len(remaining) == 2 and sum(parties) == 2 * size_of_largest:
            a, b = remaining
            output.append(ascii_uppercase[a] + ascii_uppercase[b])
            parties[a] -= 1
            parties[b] -= 1
        else:
            # Get the party with the max number of senators
            a = max(range(no_parties), key=lambda i: parties[i])
            parties[a] -= 1
            output.append(ascii_uppercase[a])

    print("Case #{}: {}".format(_, " ".join(output)))


