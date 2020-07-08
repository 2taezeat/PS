N = int(input())
A = [ 0 for i in range(N)]
S = []

for i in range(N):
    S.append(list(map(int,input().split())))


if N == 2:
    A[0] = 1
    A[1] = 1
    for i in range(N):
        print( A[i], end=' ')

else:
    for k in range(1,N):
        for m in range(k+1,N):

            a = S[0][k]-S[0][m]

            A[k] = (a + S[k][m]) // 2
            A[m] = ((-a) + S[k][m]) // 2
            A[0] = S[0][k] - A[k]



    for i in range(N):
        print( A[i], end=' ')