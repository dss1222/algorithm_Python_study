def solution(lottos, win_nums):
    zero = 0
    cnt = 0
    for i in lottos:
        if i == 0:
            zero += 1
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
    answer = []
    answer.append(rank(cnt + zero))
    answer.append(rank(cnt))

    return answer


def rank(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
