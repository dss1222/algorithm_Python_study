# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

#접두사 합 배열 계산
sum_value = 0
perfix_sum = [0]
for i in data:
    sum_value += i
    perfix_sum.append(sum_value)

#구간 합 계산 (세번째 조합 수부터 네번째 수까지)
left = 3
right = 4
print(perfix_sum[right] - perfix_sum[left - 1])
