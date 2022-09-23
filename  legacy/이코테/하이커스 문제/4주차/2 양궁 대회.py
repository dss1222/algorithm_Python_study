def solution(n, info):
    score = 0
    for i in range(len(info)):
        if info[i]:
            score -= (10-i)
    print(score)
    answer = []
    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
#어피치가 유리함
#k점을 어피치와 라이언이 맞추면 더 많이 맞춘쪽이 점수를 가져감