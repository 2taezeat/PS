import sys
N = int(sys.stdin.readline())
list1 = list (map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [[False] * (N) for i in range(N)] # dp[N][N]

for i in range(N): # d =0
    dp[i][i] = True

for i in range(N-1):
    if list1[i] == list1[i+1]: # d = 1
        dp[i][i+1] = True

for i in range(N-2):
    if list1[i] == list1[i+2]: # d = 2
        dp[i][i+2] = True

# d = 3 이상부터
for d in range(3,N):
    for i in range(0, N-d ):

        if ( (list1[i] == list1[i+d]) & dp[ i+1 ][ d+i-1 ] ) :
            dp[i][d+i] = True

for i in range(M):
    S, E = map(int,sys.stdin.readline().split())

    if (dp[S-1][E-1]) == True:
        print(1)
    else:
        print(0)