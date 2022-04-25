s = "abcde"
S = list(s)
if len(s) % 2 ==0:
    idx = len(S)//2
    print(f'"{S[idx-1]}{S[idx]}"')
else:
    idx = len(S) // 2
    print(S[idx])
