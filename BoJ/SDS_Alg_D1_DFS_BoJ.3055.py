from collections import deque
r, c = map(int,input().split())
map1 = []
for i in range(r):
    a = list(input())
    map1.append(a)
dp = [[0]*c for _ in range(r)] # 몇번째로 도착했는지
dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]
foundanswer = False

def checkSafe(y,x): # X가 아니고, *아니고, *에 인접한 .도 아니고 체크
    if map1[y][x] == 'D':
        return True

    elif map1[y][x] == '.':

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if ( 0<= ty < r) & (0 <= tx < c):
                if (map1[ty][tx] == '*'):
                    return False
        
        return True
    else:
        return False

q, wq = deque(), deque()

for j in range(r):
    for i in range(c):
        
        if map1[j][i] == "S":
            q.append( [j,i,"S"] )

        elif map1[j][i] == "*":
            wq.append( [j,i,'*'] )

q = q + wq

while ( q ):
    p = q.popleft()

    if p[2] == "D": # 목적지인가?
        print( dp[p[0]][p[1]] )
        foundanswer = True
        break

    for i in range(4):
        tx = p[1] + dx[i]
        ty = p[0] + dy[i]

        if (0<= ty < r) & (0 <= tx < c):
            if (p[2] == '.') or (p[2] == 'S'):
                
                if (dp[ty][tx] == 0) & (checkSafe(ty,tx)):

                    dp[ty][tx] = dp[p[0]][p[1]] + 1
                    q.append( [ ty, tx, map1[ty][tx] ] )
        
            elif (p[2] == '*') and (map1[ty][tx] == '.'):
                q.append( [ ty, tx, '*' ] )
                map1[ty][tx] = '*'

if foundanswer == False:
    print("KAKTUS")