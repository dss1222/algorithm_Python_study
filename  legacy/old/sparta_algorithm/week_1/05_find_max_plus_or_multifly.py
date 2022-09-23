input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result1 = 0
    for i in array:
        if result1==0:
            result1 += i
            print(result1, "0dle")
        elif i <= 1:
            result1 += i
            print(result1, "1보다 작다")
        else:
            result1 *= i
            print(result1)

    return result1


result = find_max_plus_or_multiply(input)
print(result)