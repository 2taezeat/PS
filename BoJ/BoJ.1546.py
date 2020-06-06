n = int(input())
sl = list(map(int,input().split()))
M = max(sl)
for i in range(n):
    sl[i] = sl[i]/M*100


print(sum(sl)/n)