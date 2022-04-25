n = 5 #데이터 개수
m = 5 # 찾고자하는 부분 합
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n): #start를 차례대로 증가시키며 반복
    while interval_sum < m and end < n:
        #end를 가능한 만큼 이동시키기
        interval_sum += data[end]
        end += 1
    #부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count +=1
    interval_sum -= data[start]

print(count)