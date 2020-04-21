t = int(input())

for i in range(t):
    s = input()

    for k in range(1,len(s)):
        if s.find(s[k-1]) > s.find(s[k]):
            t = t - 1
            break
    
print(t)

## str.find 를 얻어갈수있는 문제