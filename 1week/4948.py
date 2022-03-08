def sosu(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for n in range(n, 2 * n + 1):
        if sosu(n):
            count += 1
    print(count)
