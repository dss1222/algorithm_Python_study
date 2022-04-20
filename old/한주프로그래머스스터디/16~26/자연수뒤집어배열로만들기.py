def solution(n):
    answer = []
    s = str(n)
    for i in s:
        answer.append(int(i))
    answer.reverse()
    return answer


n = [1, 2, 3, 4, 5]
print(solution(n))
