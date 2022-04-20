def solution(n):
    answer = ''
    array = list(str(n))
    array.sort(reverse=True)
    for i in array:
        answer += str(i)
    return answer

n = 118372
print(solution(n))