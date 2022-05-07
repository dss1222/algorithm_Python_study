a, b = map(int, input().split())

def gcd(a, b):  # 최대공약수
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def lcm(a, b):
    baesu = (a * b) / gcd(a, b)
    return baesu


print(gcd(a, b))
print(int(lcm(a, b)))