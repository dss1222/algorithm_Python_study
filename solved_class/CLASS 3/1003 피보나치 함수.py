cnt0 = [1, 0]
cnt1 = [0, 1]

test_round = int(input())

for i in range(test_round):
    test_case = int(input())

    if test_case == 0:
        print("1 0")
    elif test_case == 1:
        print("0 1")
    else:
        for j in range(2, test_case+1):
            cnt0.append(cnt0[j-1] + cnt0[j-2])
            cnt1.append(cnt1[j-1] + cnt1[j-2])
        print(f"{cnt0.pop()} {cnt1.pop()}")
        cnt0 = [1, 0]
        cnt1 = [0, 1]