from collections import Counter


def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []
    # str1 과 str2 매개변수 전처리,
    # 대문자와 소문자의 차이는 무시하고, 영문자로 이루어진 조합의 경우에만 사용
    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])
    # 카운터 객체로 변환
    # 각각의 리스트는 해당 원소값을 key값으로, 원소의 갯수를 value 값으로하는 dictionary형태 구조
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    # elements메서드는 딕셔너리의 원소값만 추출
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
