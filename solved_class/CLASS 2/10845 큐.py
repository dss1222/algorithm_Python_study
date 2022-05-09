from collections import deque
import sys

n = int(input())
q = deque()

for i in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        q.append(word[1])
    elif word[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif word[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])