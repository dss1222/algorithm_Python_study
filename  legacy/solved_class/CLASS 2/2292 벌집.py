n = int(input())
cnt=0
num = 1
while True:
    num += 6*cnt
    cnt += 1
    if n <= num:
        break
print(cnt)