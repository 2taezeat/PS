n = int(input())
xyl = []
for i in range(n):
    x,y = map(int,input().split())
    xyl.append([x,y])

xyl = sorted(xyl, key = lambda x : (x[1], x[0]))

for i in range(n):
    print(xyl[i][0],xyl[i][1])