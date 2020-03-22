N , M = map(int,input().split())
space = [ [0 for i in range(M+1)] ] 
for i in range(N):
    space.append([0]+list(map(int,input().split())))

for y in range(1,N+1):
    for x in range(1,M+1):
        max1 = max( space[y-1][x], space[y][x-1] , space[y-1][x-1] )
        space[y][x] = max1 + space[y][x]

print(space[-1][-1])