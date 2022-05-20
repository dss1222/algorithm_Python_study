def solution(N, stages):
    fail_rate = {}
    total_user = len(stages)

    for stage in range(1, N+1):
        if total_user != 0:
            fail_user = stages.count(stage)
            fail_rate[stage] = fail_user / total_user
            total_user -= fail_user
        else:
            fail_rate[stage] = 0
    print(fail_rate)
    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])