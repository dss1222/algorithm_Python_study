def solution(s):
    answer = ''
    y = s.split(' ')
    for i in y:
        for j in range(len(i)):
            if j % 2 == 1:
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += ' '
    return answer[0:-1]


s = "try hello world"
print(solution(s))
