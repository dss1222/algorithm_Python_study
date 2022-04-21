def solution(numbers):
    set_list = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            set_list.add(numbers[i] + numbers[j])

    return sorted(list(set_list))


print(solution([2, 1, 3, 4, 1]))
