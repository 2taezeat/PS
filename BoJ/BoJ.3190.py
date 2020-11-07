# 구현_2_이태경.py
from collections import deque
# input 받기
n = int(input())
k = int(input())
apple_list = []
snake_d = deque()
space = []
for i in range(k):
    apple_list.append(list(map(int,input().split())))
l = int(input())
for i in range(l):
    a, b = input().split()
    snake_d.append( [a,b])

x,y,snake_len = 1,1,1 # 뱀의 첫번째 위치
time = 0
d = 0 # d가  0: -> / 1:아래 / 2: <- / 3:위  ........... 처음에는 ->(d=0)
for i in range(n+2):
    space.append([0]*(n+2))
for i in range(n+2):
    for j in range(n+2):
        if i == 0 or j == 0 or i == n+1 or j == n+1:
            space[i][j] = 1 # 벽 = 1, 빈칸 = 0, 사과 = 3,뱀의 몸통 = 4 ,뱀의 머리 = 5
        else:
            continue
for a,b in apple_list: # space에 사과가 존재하는 좌표에 3 할당
    space[a][b] = 3

dx = [0,1,0,-1]
dy = [1,0,-1,0]
space[x][y] = 5
q = deque()
q.append([x,y])

def change_direction(cd, nd):
    if cd == 'L':
        nd = ( nd - 1 ) % 4
    elif cd == 'D':
        nd = ( nd + 1 ) % 4

    return nd

while(True):
    # snake_d 큐에서 가장 왼쪽에 있는(0) 값을 꺼냄. 모두 꺼내서 q = []일때, 스네이크가 벽에 안붙히치면, 큐에서 꺼낼것이없으므로 에러가나서 try문 사용
    try:
        count_time, change_d = snake_d[0][0], snake_d[0][1]
    except:
        pass
    
    # time이 방향변환을 해야할 시간이면 change_direction 함수로 반환 전환
    if time == int(count_time):
        d = change_direction(change_d, d)
        snake_d.popleft()

    nx = x + dx[d]
    ny = y + dy[d]
    # q는 스네이크의 몸통과 머리가 존재하는 좌표를 담고있고, q[-1]가 스네이크의 머리 좌표임.
    if 0 < nx < n+1 and 0 < ny < n+1 and space[nx][ny] != 4: # 다음 좌표가 벽에 붙히치지 않고, 몸통에도 붙히치지 않으면
        if space[nx][ny] == 3: # 이동한 칸에 사과가 있다면

            a,b = q.pop()
            q.append([x,y])
            q.append([nx,ny])

            x = nx
            y = ny

        else: # 이동한 칸에 사과가 없다면

            a, b = q.popleft()
            space[a][b] = 0
            q.append([nx,ny])

            x = nx
            y = ny
    
    else:
        time = time + 1
        break
    # q의 q[-1]를 제외한 부분은 몸통 부분임으로 해당하는 좌표에 4값을 할당.
    for i in range( len(q) - 1 ):
        a, b = q[i][0], q[i][1]
        space[a][b] = 4
    # q의 머리부분의 좌표는 5로 할당.
    space[q[-1][0]][q[-1][1]] = 5

    time = time + 1
    #print('time',time)
    #space_print()
    #print('--------------------------------------')

print(time)