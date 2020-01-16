N = int(input())
P = list(map(int,input().split()))

P.sort()

sum = 0
c = 0
for i in range(N-1,-1,-1):
    c = c + 1
    sum = sum + P[i]*c

print(sum)