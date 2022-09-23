import sys

n = int(sys.stdin.readline())

check = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    check[num] = check[num] + 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)