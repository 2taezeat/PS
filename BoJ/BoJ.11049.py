import sys
N = int(sys.stdin.readline())
rlist = []
clist = []
dp = [[0] * (N) for i in range(N)] 
for i in range(N):
    r, c = map(int,sys.stdin.readline().split())
    rlist.append(r)
    clist.append(c)

for i in range(1,N):
    for j in range(0,N-i):

        alist = []
        for k in range(j,j+i,1):
            a = dp[j][k] + dp[k+1][j+i] + (rlist[j]*clist[k]*clist[j+i])
            alist.append(a)
            
        if alist != []:
            dp[j][j+i] = min(alist)  
print(dp[0][N-1])