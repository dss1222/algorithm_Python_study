def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # or 연산 |임. 문제에서 둘중 하나라도 #(1)이면 #(1)이므로 or 계산을 함
        tmp = bin(arr1[i] | arr2[i])
        print(tmp)
        # tmp결과 ex) '0b1101'
        # zfill은 글자수가 n보다 부족하다면 부족한만큼 앞에 0으로 채워준다
        tmp = tmp[2:].zfill(n)
        print(tmp)
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1', '#').replace('0', ' ')
        print(tmp)
        # tmp결과 ex) ' ## #'
        answer.append(tmp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
