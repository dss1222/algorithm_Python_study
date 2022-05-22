a = [False, False] + [True]*(999999)
primes = []


def solution(n, k):
    eratones()
    sosu = convert(n, k)
    word = ''
    stack = []
    remove_set = {'1', ''}
    cnt = 0
    i = 0
    while True:
        if i == len(sosu):
            stack.append(word)
            break
        elif sosu[i] != '0':
            word += str(sosu[i])
            i += 1
        elif sosu[i] == '0':
            stack.append(word)
            word = ''
            i += 1

    stack = [i for i in stack if i not in remove_set]

    for i in stack:
        if primes[int(i)]:
            cnt += 1
    return cnt


def convert(n, k):
    answer = ''

    while n > 0:
        answer = str(n % k) + answer
        n = n // k
    return answer


def eratones():
    for i in range(2, 1000001):
        if a[i]:
            primes.append(i)
            for j in range(2*i,1000001,i):
                a[j] = False


solution(437674, 3)
