n = int(input())

sugar = [5, 3]
count = 0
while n > 3:
    for i in sugar:
        count += n//i
        n %= i

if n==0:
    print(count)
else:
    print(-1)
