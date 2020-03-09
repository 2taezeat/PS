N, M = map(int,input().split() )
space = []
for i in range(N):
    space.append( list(map(int,input().split() )))
result = []

for y in range(N):
    for x in range(M-3):
        sum1 = 0
        sum1 = space[y][x] + space[y][x+1] + space[y][x+2] + space[y][x+3]
        result.append(sum1) 
for y in range(N-3):
    for x in range(M):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y+2][x] + space[y+3][x]
        result.append(sum1) 
for y in range(N-1):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x+1] + space[y+1][x] + space[y][x+1]
        result.append(sum1) 
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y][x] + space[y][x+1] + space[y][x+2] + space[y+1][x+1]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y+1][x] + space[y+1][x+1] + space[y][x+1] + space[y+1][x+2]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y+1][x] + space[y][x+1] + space[y+1][x+1] + space[y+2][x+1]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y+1][x+1] + space[y+2][x]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y+1][x+1] + space[y+2][x+1]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x+1] + space[y+1][x] + space[y+1][x+1] + space[y+2][x]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y+1][x] + space[y+1][x+1] + space[y][x+1] + space[y][x+2]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x+1] + space[y][x+1] + space[y+1][x+2]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y][x+1] + space[y][x+2]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y+1][x] + space[y+1][x+1] + space[y+1][x+2] + space[y][x+2]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x+1] + space[y+1][x] + space[y+1][x+2]
        result.append(sum1)
for y in range(N-1):
    for x in range(M-2):
        sum1 = 0
        sum1 = space[y][x] + space[y][x+1] + space[y][x+2] + space[y+1][x+2]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y+2][x] + space[y+2][x+1]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x+1] + space[y+1][x+1] + space[y+2][x] + space[y+2][x+1]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y+1][x] + space[y+2][x] + space[y][x+1]
        result.append(sum1)
for y in range(N-2):
    for x in range(M-1):
        sum1 = 0
        sum1 = space[y][x] + space[y][x+1] + space[y+1][x+1] + space[y+2][x+1]
        result.append(sum1)

print(max(result))