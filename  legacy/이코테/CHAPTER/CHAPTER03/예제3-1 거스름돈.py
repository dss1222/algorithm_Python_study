# price = int(input())
# won500 = price//500
# won100 = (price - won500 * 500) // 100
# won50 = (price - won500 * 500 - won100 * 100) // 50
# won10 = (price - won500 * 500 - won100 * 100 - won50 * 50) // 10
# count = won500 + won100 + won50 + won10
# print(count)
#

n = int(input())
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)