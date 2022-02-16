n = int(input())
test_list = list(map(int, input().split()))
max = max(test_list)
new_list = []
for score in test_list:
    new_list.append(score/max*100)
result = sum(new_list)/n
print(result)