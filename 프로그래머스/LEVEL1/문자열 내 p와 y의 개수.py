def solution(s):
    cnt = 0
    s = list(s.lower())
    for i in s:
        if i == 'p':
            cnt += 1
        elif i == 'y':
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False


print(solution("Pyy"))
