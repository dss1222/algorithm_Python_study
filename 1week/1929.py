#1을 먼저 제거, 지워지지 않는 수중 제일 작은 수를 소수로 선택
#2의배수를 제거, 지워지지 않는 수중 제일 작은 수를 소수로 선택
#3의 배수를 제거, 지워지지 않는 수중 제일 작은 수를 소수로 선택 >> 반복
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i ==0:
                return False
            return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i):
        print(i)