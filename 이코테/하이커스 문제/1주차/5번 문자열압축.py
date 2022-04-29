def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):  # 쪼개기 1번~길이/2번까지
        b = ''
        cnt = 1
        tmp = s[:i]  # 문자열 쪼갤 부분 앞을 담음

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