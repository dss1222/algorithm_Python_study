import sys

n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))

time.sort()
print(time)
result=0
for i in range(len(time)):
    hap = 0
    for j in time[0:i+1]:
        hap += j
    print(hap)
    result += hap

print(result)