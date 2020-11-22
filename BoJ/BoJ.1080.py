def change(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if a[i][j]==0:
                a[i][j]=1
            else:
                a[i][j]=0

n,m=map(int,input().split())
a=[list(map(int,list(input()))) for i in range(n)]
b=[list(map(int,list(input()))) for i in range(n)]


ans=0
for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j]!=b[i][j]:
            change(i,j)
            ans+=1
check=True
for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            check=False
if check:
    print(ans)
else:
    print(-1)