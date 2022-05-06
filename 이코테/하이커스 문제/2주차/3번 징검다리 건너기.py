def solution(stones, k):
    start, end = min(stones), max(stones)
    #이진 탐색
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in stones:
            if i - mid <= 0 :
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1

    return start


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
