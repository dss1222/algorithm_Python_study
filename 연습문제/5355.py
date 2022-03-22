n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    answer = 0
    for _ in range(len(x)):
        if _ == 0:
            answer += float(x[_])
        else:
            if x[_]=='#':
                answer -= 7
            if x[_]=='%':
                answer += 5
            if x[_]=='@':
                answer *= 3
    print("%0.2f" % answer)
