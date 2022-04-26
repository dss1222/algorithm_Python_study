def solution(s):
    result = []  # 1,2,3,....n/2씩 쪼갠 길이를 담는 리스트
    if len(s) == 1:  # 길이가 1이면 그냥 1 리턴
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp

        result.append(len(b))
    return min(result)


print(solution('aabbaccc'))
