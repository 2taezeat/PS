import sys
T = int(sys.stdin.readline())
Klist = []
filelist = []

for m in range(T):
    K = int(sys.stdin.readline())    
    Klist.append(K)
    flist = list(map(int, sys.stdin.readline().split()))
    filelist.append(flist)
    dp = [ [0] * (K) for i in range(K)]

    for i in range(1,K):
        for j in range(0,K-i):
                
            alist = []
            for k in range(j,j+i,1):
                a = dp[j][k] + dp[k+1][j+i]
                alist.append(a)

            if alist != []:
                dp[j][j+i] = min(alist) + sum( flist[j:j+i+1] ) 

    print(dp[0][K-1])