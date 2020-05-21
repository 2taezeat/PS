a, i = map(int,input().split())

p = a*i
c = 0
for k in range(p,-1,-1):
    if (k/a) <= i-1 :
        c = k
        break

print(c+1)
