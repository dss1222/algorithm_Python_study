def solution(ls):
    return min(len(ls)//2, len(set(ls)))

print(solution([3,3,3,2,2,4]))