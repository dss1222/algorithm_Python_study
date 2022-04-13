input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha = [0]*26
    for i in string:
        if not i.isalpha():
            continue
        arr_idx = ord(i)-ord("a")
        alpha[arr_idx] += 1

    print(max(alpha))
    return string[max(alpha)]


result = find_max_occurred_alphabet(input)
print(result)