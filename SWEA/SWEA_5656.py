import copy
from collections import deque
from itertools import product
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,w,h = map(int,input().split())
    space = []
    for i in range(h):
        space.append(list(map(int,input().split())))
    l1 = [i for i in range(w)] # per을 만들기 위한 리스트 l1
    per = []
    for i in product(l1, repeat=n):
        per.append(i)

    answer = []
    for p in per:
        c_space = copy.deepcopy(space)
        count = 0 # 터지는 폭탄 count
        for t in p:

            Q = deque()
            for j in range(h):
                if c_space[j][t] != 0:
                    count = count + 1
                    power = c_space[j][t]
                    Q.append([power,j,t])

                    c_space[j][t] = 0

                    while (Q):
                        bomb_power,y,x = Q.popleft()
                        for b_p in range(1,bomb_power):

                            for i in range(4):
                                ny = y + (dy[i] * b_p)
                                nx = x + (dx[i] * b_p)

                                if 0 <= ny < h and 0 <= nx < w and c_space[ny][nx] != 0 :
                                    Q.append( [ c_space[ny][nx], ny, nx ] )
                                    count = count + 1
                                    c_space[ny][nx] = 0
                    
                    break

            for i in range(h-2,-1,-1):
                for j in range(w):
                    if c_space[i][j] != 0 and c_space[i+1][j] == 0:

                        for k in range(i+1,h):
                            
                            if k == h-1 and c_space[k][j] == 0:
                                c_space[k][j] = c_space[i][j]

                            elif c_space[k][j] != 0:
                                c_space[k-1][j] = c_space[i][j]
                                break

                        c_space[i][j] = 0

        remain = 0
        for i in range(h):
            for j in range(w):
                if c_space[i][j] != 0:
                    remain = remain + 1

        answer.append((count,remain))

    print('#',end='')
    print('{0} {1}'.format(test_case,max(answer)[1]))