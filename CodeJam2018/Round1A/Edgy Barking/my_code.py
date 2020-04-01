"""
    ogni rettangolo ha 3 possibili tagli,
    loopare tra i rettangoli fino a che non si è ragginunta la somma
    richiesta(o si è vicini alla somma richiesta)
"""
import math


#
def largest_sum(p, cookies):
    tot = 0

    for cookie in cookies:
        p2 = 2*cookie[0] + 2*cookie[1]
        sum_h = (4 * cookie[0] / 2 + 4 * cookie[1])
        sum_w = (4 * cookie[1] / 2 + 4 * cookie[0])
        sum_d = 2 * (cookie[0] + cookie[1] + math.sqrt(math.pow(cookie[0],2) + math.pow(cookie[1],2)))

        tot_0 = tot+p2 if tot+p2 <= p else 0
        tot_1 = tot + sum_h if tot + sum_h <= p else 0
        tot_2 = tot + sum_w if tot + sum_w <= p else 0
        tot_3 = tot + sum_d if tot + sum_d <= p else 0

        tot = max(tot_0,tot_1, tot_2, tot_3)

    return tot


for case in range(int(input())):
    n, p = map(int, input().split())
    cookies = []

    for i in range(n):
        cookies.append(tuple(map(int, input().split())))

    print("Case #{}: {}".format(case + 1, largest_sum(p, cookies)))
