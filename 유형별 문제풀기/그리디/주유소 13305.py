n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
m = price[0]
min_price = min(price)
sum_distance = sum(distance)
for i in range(n-1):
    if price[i] < m:
        m = price[i]
    res += m*distance[i]

print(res)