def solution(d, budget):
    answer = budget
    cnt = 0
    d.sort()
    for i in d:
        if answer >= i:
            cnt += 1
            answer -= i
    return cnt

print(solution([1,3,2,5,4], 9))