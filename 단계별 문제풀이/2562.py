arr = []
for i in range(9):
    arr.append(int(input()))

max = max(arr)
print(max)
idx = arr.index(max)
print(idx + 1)