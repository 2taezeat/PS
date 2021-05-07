# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위'혹은 '다른 기둥 위'라면 정상
            if ( y == 0  ) or ( [x - 1, y, 1] in answer ) or ( [x, y, 1] in answer ) or ( [x, y - 1, 0] in answer ):
                continue
            return False # 아니라면 False
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 False
    return True



def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제 연산을 진행
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 불가능하면 다시 넣어주기

        if operate == 1 : # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치해본 다음에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 제거
    return sorted(answer) # 정렬된 결과를 반환


###################
def solution(n, build_frame):
    space = [ [[0,0] for i in range(n+1)] for i in range(n+1)]
    for (x,y,a,b) in build_frame:
        if b == 1: # 설치
            if a == 0:
                if (y == 0) or (space[y][x][0] == 3) or (space[y][x][1] == 4):
                    space[y][x][0] += 3
                    space[y+1][x][0] += 3

            elif a == 1:
                if (space[y][x][0] == 3) or (space[y][x+1][0] == 3) or (space[y][x][1] == 4 and space[y][x+1][1] == 4 ):
                    space[y][x][1] += 4
                    space[y][x+1][1] += 4

        elif b == 0: # 삭제
            if a == 0:
                space[y][x][0] -= 3
                space[y+1][x][0] -= 3

                flag = True
                for i in range(n): # 전체 검사
                    for j in range(n):
                        if flag == False:
                            break
                        if (space[i][j][0] >= 3) and not ( (i == 0) or (space[i][j][0] >= 3) or (space[i][j][1] >= 4) ):
                            #print('type1')
                            flag = False
                        if (space[i][j][1] >= 4 ) and not ( (space[i][j][0] >= 3) or (space[i][j+1][0] >= 3) or (space[i][j][1] >= 4 and space[i][j+1][1] >= 4 ) ):
                            flag = False
                            #print('type2',i,j)
                    if flag == False:
                        break


                if flag == False: # 일단 수행후, 위반하면 원상복귀
                    space[y][x][0] += 3
                    space[y+1][x][0] += 3

            elif a == 1:
                space[y][x][1] -= 4
                space[y][x+1][1] -= 4
                flag = True
                for i in range(n): # 전체 검사
                    for j in range(n):
                        if flag == False:
                            break
                        if (space[i][j][0] >= 3) and not ( (i == 0) or (space[i][j][0] >= 3) or (space[i][j][1] >= 4) ):
                            #print('type1')
                            flag = False
                        if (space[i][j][1] >= 4 ) and not ( (space[i][j][0] >= 3) or (space[i][j+1][0] >= 3) or (space[i][j][1] >= 4 and space[i][j+1][1] >= 4 ) ):
                            #print('type2',i,j)
                            flag = False
                    if flag == False:
                        break
                #print(flag)

                if flag == False: # 일단 수행후, 위반하면 원상복귀
                    space[y][x][1] += 4
                    space[y][x+1][1] += 4

            print(flag)

        for i in range(n+1):
            print(space[i])
        print('-------------')

    rlend = []
    for i in range(0,n):
        for j in range(0,n):
            if space[i][j][0] == 3 and space[i+1][j][0] == 3:
                rlend.append([j,i,0])
            if space[i][j][1] == 4 and space[i][j+1][1] == 4:
                rlend.append([j,i,1])

    for i in range(0,n):
        if space[i][n][0] == 3 and space[i+1][n][0] == 3:
            rlend.append([n,i,0])

    rlend.sort(key= lambda x  : (x[0], x[1], x[2]))
    return rlend

#print(solution(5,	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	))