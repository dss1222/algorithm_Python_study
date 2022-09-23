import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = {0: 0}

for _ in range(N):
    curr_w, curr_v = map(int, read().split())
    temp = {}
    for w, v in cache.items():
        if curr_w + w <= K and curr_v + v > cache.get(curr_w + w, 0):
            temp[curr_w + w] = curr_v + v
    cache.update(temp)
print(max(cache.values()))