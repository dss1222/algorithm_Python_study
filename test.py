def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += price * i

    if sum-money <= 0:
        return 0
    else:
        return sum-money

print(solution(3, 32, 4))