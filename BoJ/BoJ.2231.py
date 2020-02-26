N = int(input())
result = 0
for i in range(1,N+1):
    s = str(i)
    r = 0
    for d in s:
        r = r + int(d)
        
    r = r + i

    if r == N:
        result = i
        break

print(result)