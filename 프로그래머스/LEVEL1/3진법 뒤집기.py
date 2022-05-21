def solution(n):
    answer = ''

    while n > 0:
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return answer

print(solution(437674))