x, y, w, h = map(int,input().split())
list1 = [x, y, w-x, h-y]

print(min(list1))