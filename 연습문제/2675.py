n = int(input())
for i in range(n):
    number, string = input().split()
    text = ""
    for j in range(len(string)):
        text += string[j]*int(number)
    print(text)
