import math

n = int(input())

for i in range(n): #맨 첫줄입력받은 수 몇번 반복할지
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리
    if distance == 0 and r1 == r2 :  # 두 원이 겹칠 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 접점이 하나일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에
