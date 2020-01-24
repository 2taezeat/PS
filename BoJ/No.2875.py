N,M,K = map(int,input().split())

X = 0
for i in range(K+1):
    j= K-i
    newN = N - i
    newM = M - j

    if newN>=2*newM:
        X = newM
    if newN < 2 * newM:
        X = newN//2

    if i ==0:
        maxX= X
    maxX = max(maxX,X)


print(maxX)