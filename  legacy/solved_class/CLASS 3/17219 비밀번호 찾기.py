import sys

input = sys.stdin.readline

N, M = map(int, input().split())
add = {}
#저장을 딕셔너리로 하고 사이트를 키값으로 지정해준다.
for _ in range(N):
    site, ps = input().split()
    add[site] = ps

for _ in range(M):
    print(add[input().rstrip()])