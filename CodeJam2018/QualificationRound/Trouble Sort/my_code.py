t = int(input())

for _ in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ## Get the even_list form by all the number in numbers with an even index
    even_list = numbers[::2]
    ## Get the odd_list form by all the number in numbers with an odd index
    odd_list = numbers[1::2]

    #Sort the two lists
    even_list.sort()
    odd_list.sort()

    numbers = []

    # Use enumerate to insert odd elements in the even_list
    for i, v in enumerate(odd_list):
        even_list.insert(2 * i + 1, v)

    res = 'OK'

    # Check the first element unsorted
    for i in range(0, len(even_list) - 1):
        if even_list[i] > even_list[i + 1]:
            res = i
            break

    print("Case #{}: {}".format(_, res))
