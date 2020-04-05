t = int(input())


def fits_in_schedule(p_schedule, activities, i):
    if len(p_schedule) == 0:
        p_schedule.append(activities[i])
        return True

    for j in range(0, len(p_schedule)):
        if p_schedule[j][0] <= activities[i][0] < p_schedule[j][1]:
            return False
        elif p_schedule[j][0] < activities[i][1] <= p_schedule[j][1]:
            return False

    p_schedule.append(activities[i])
    return True


for case in range(1, t + 1):
    n = int(input())
    activities = []
    c_activities = []
    j_activities = []
    res = "C"

    for i in range(n):
        activities.append(tuple(map(int, input().split())))

    c_activities.append(min(activities, key=lambda n: (n[0], -n[1])))

    for i in range(1, len(activities)):
        if fits_in_schedule(c_activities, activities, i):
            res += 'C'
        elif fits_in_schedule(j_activities, activities, i):
            res += 'J'
        else:
            res = 'IMPOSSIBLE'
            break

    print('Case #{}: {}'.format(case, res))
