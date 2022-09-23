cnt = int(input())
number = list(map(int, input().split()))
max = number[0]
min = number[0]
for i in number[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)