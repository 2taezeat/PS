# 구현_3_이태경.py
def solution(n, build_frame):
    space = [[0] * (n+1) for i in range(n+1)]
    for l in build_frame:

        x, y, k, s = l[0], l[1], l[2], l[3] #x,y는 좌표 , k는 종류, s는 설치여부
        if s == 1:

            if k == 0:

                if x != 0 and space[x][y] != 4 and space[x][y] != 3:
                    continue
                else:
                    space[x][y] = 3
            elif k == 1:

                if space[x-1][y] != 3 and (space[x][y-1] != 4 or space[x][y+1] != 4):
                    continue
                else:
                    space[x][y] = 4

        else:
            # if k == 0:
                
            #     if space[x+1][y] == 4 or space[x+1][y] == 3:
            #         continue

            # elif k == 1:

            space[x][y] = 0

    
    print(space)

    space[0]








print( solution(5, [ [1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1] ] ))