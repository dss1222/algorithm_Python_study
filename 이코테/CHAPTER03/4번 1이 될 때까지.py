# n, k = map(int, input().split())
# i = 1
# count = 0
# while n > 1:
#     if n % k != 0:
#         n -= i
#         i += 1
#         count += 1
#     if n % k == 0:
#         n /= k
#         count += 1
#
# print(count)

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)