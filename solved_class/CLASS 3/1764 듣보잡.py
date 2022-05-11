n, m = map(int,input().split())
#set은 중복이 없는 특성 add로 추가한다
a = set()
for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())
# set a, b 의 교집합 &을 해서 중복되는 문자열을 선택하고 list()로 리스트화 시킴
result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)