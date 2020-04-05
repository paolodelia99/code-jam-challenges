for case in range(1, int(input()) + 1):
    s = input()
    rest_close_par = 0
    res = ''

    if len(s) == 1:
        res = '('*(int(s[0]))+s[0]+')'*(int(s[0]))
    else:
        for i in range(0, len(s)):
            # check the first element
            if i == 0 and int(s[i]) != 0:
                res += ('(' * (int(s[i]))) + s[i]
            elif i == 0 and int(s[i]) == 0:
                res += s[i]
            # Check for the last element
            elif i == len(s) - 1:
                if s[i-1] == s[i]:
                    res += s[i] + ')' * (int(s[i]))
                elif int(s[i-1]) < int(s[i]):
                    res += '('*(int(s[i])-int(s[i-1]))+s[i]+')'*(int(s[i]))
                elif int(s[i-1]) > int(s[i]):
                    res += ')' * (abs(int(s[i-1]) - int(s[i]))) + s[i] + ')' * (int(s[i]))
            # Check for the other element
            else:
                if s[i - 1] == s[i]:
                    res += s[i]
                elif int(s[i - 1]) > int(s[i]):
                    res += (')' * (int(s[i - 1]) - int(s[i]))) + s[i]
                else:
                    res += ('(' * (int(s[i]) - int(s[i-1]))) + s[i]

    print('Case #{}: {}'.format(case, res))
