'''
내가 푼 것
N = 1260
x, y, a, z = 0, 0, 0, 0

x = N//500
N = N - 500*x
y = N//100
N = N - 100*y
a = N//50
N = N - 50*a
z = N//10
N = N - 10*z
print(x+y+a+z)
'''
n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin # 왼쪽 변수에 오른쪽 값을 나누고 그 결과를 왼쪽 변수에 할당한다

print(coin)