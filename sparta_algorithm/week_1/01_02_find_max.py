input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for i in array:
        if max_num < i:
            max_num = i

    # 이 부분을 채워보세요!
    return max_


result = find_max_num(input)
print(result)
