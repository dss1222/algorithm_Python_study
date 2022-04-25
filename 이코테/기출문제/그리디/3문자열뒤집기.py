s = input()
oneCnt=0
zeroCnt=0

if s[0] == '1':
    zeroCnt += 1
else:
    oneCnt += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '1':
            zeroCnt += 1
        else:
            oneCnt += 1

print(min(oneCnt, zeroCnt))

