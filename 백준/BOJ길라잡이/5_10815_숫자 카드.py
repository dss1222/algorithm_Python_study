import sys
n = int(sys.stdin.readline())
have = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = ""
for i in arr:
    if i in have:
        answer += '1 '
    else:
        answer += '0 '
print(answer)