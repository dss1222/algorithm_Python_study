def solution(dartResult):
    answer = []
    score = {'S': 1, 'D': 2, 'T': 3}

    cur = -1
    idx = -1
    for i in dartResult:

        if i in ['S', 'D', 'T']:
            answer[idx] = answer[idx] ** score[i]
        elif i == '*':
            answer[idx] *= 2
            if idx != 0:
                answer[idx - 1] *= 2
        elif i == '#':
            answer[idx] *= -1
        else:
            if int(i) == 0 and cur == 1:
                cur = 10
                answer.pop()
                answer.append(cur)
            else:
                cur = int(i)
                answer.append(cur)
                idx += 1
    return sum(answer)