t = int(input())

for _ in range(1, t + 1):
    n = int(input())
    l_path = input()
    my_path = []

    # Find the simmetric path
    for i in range(0, len(l_path)):
        my_path.append('E' if l_path[i] == 'S' else 'S')

    my_path = "".join(my_path)

    print("Case #{}: {}".format(_, my_path))
