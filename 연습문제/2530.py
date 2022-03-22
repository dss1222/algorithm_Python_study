H, M, S = map(int, input().split())
D = int(input())

S += D % 60 #시간초 더하기
D = D // 60 #분으로 바꾸기
if S >= 60:
    S -= 60
    M += 1

M += D % 60 #분 더하기
D = D // 60 #시간으로 바꾸기
if M >= 60:
    M -= 60
    H += 1

H += D % 24 #시간 더하기
if H >= 24:
    H -= 24

print(H, M, S)
