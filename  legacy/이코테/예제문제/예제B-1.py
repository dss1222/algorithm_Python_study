import math

m, n = map(int, input().split())

array = [True for i in range(1000001)]
array[1] = 0

for i in range(2, int(math.sqrt(n))+1): #2부터 n의 제곱근까지 모든 수를 확인
    if array[i] == True: #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i]:
        print(i)