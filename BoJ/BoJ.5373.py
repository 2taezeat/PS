TC = int(input())
def change(s,d,cu):
    if d == '-':
        if s == 'U':
            tmp = []
            for i in range(0,12):
                tmp.append(cu[3][i])

            cu[3][3] = tmp[0]
            cu[3][4] = tmp[1]
            cu[3][5] = tmp[2]

            cu[3][6] = tmp[3]
            cu[3][7] = tmp[4]
            cu[3][8] = tmp[5]

            cu[3][9] = tmp[6]
            cu[3][10] = tmp[7]
            cu[3][11] = tmp[8]

            cu[3][0] = tmp[9]
            cu[3][1] = tmp[10]
            cu[3][2] = tmp[11]
            
            # 왼쪽 -90도 회전
            arr = []
            for i in range(0,3):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(0,3):
                for j in range(3,6):
                    cu[i][j] = arr_90[i][j-3]

        elif s == 'D':
            tmp = []
            for i in range(0,12):
                tmp.append(cu[5][i])
            cu[5][0] = tmp[3]
            cu[5][1] = tmp[4]
            cu[5][2] = tmp[5]

            cu[5][3] = tmp[6]
            cu[5][4] = tmp[7]
            cu[5][5] = tmp[8]

            cu[5][6] = tmp[9]
            cu[5][7] = tmp[10]
            cu[5][8] = tmp[11]

            cu[5][9] = tmp[0]
            cu[5][10] = tmp[1]
            cu[5][11] = tmp[2]
            
            # 왼쪽 -90도 회전
            arr = []
            for i in range(6,9):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(6,9):
                for j in range(3,6):
                    cu[i][j] = arr_90[i-6][j-3]

        elif s == 'F':
            tmp = []
            for i in range(3,6):
                tmp.append(cu[i][2])

            for i in range(3,6):
                tmp.append(cu[6][i])
            tmp.append(cu[5][6])
            tmp.append(cu[4][6])
            tmp.append(cu[3][6])

            tmp.append(cu[2][5])
            tmp.append(cu[2][4])
            tmp.append(cu[2][3])

            cu[6][3] = tmp[0]
            cu[6][4] = tmp[1]
            cu[6][5] = tmp[2]

            cu[5][6] = tmp[3]
            cu[4][6] = tmp[4]
            cu[3][6] = tmp[5]

            cu[2][5] = tmp[6]
            cu[2][4] = tmp[7]
            cu[2][3] = tmp[8]

            cu[3][2] = tmp[9]
            cu[4][2] = tmp[10]
            cu[5][2] = tmp[11]

            # 왼쪽 -90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(3,6):
                for j in range(3,6):
                    cu[i][j] = arr_90[i-3][j-3]

        elif s == 'B':
            tmp = []
            for i in range(3,6):
                tmp.append(cu[i][0])

            for i in range(3,6):
                tmp.append(cu[8][i])

            tmp.append(cu[5][8])
            tmp.append(cu[4][8])
            tmp.append(cu[3][8])

            tmp.append(cu[0][5])
            tmp.append(cu[0][4])
            tmp.append(cu[0][3])

            cu[0][5] = tmp[0]
            cu[0][4] = tmp[1]
            cu[0][3] = tmp[2]

            cu[3][0] = tmp[3]
            cu[4][0] = tmp[4]
            cu[5][0] = tmp[5]

            cu[8][3] = tmp[6]
            cu[8][4] = tmp[7]
            cu[8][5] = tmp[8]

            cu[5][8] = tmp[9]
            cu[4][8] = tmp[10]
            cu[3][8] = tmp[11]

            # 왼쪽 -90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(9,12):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(3,6):
                for j in range(9,12):
                    cu[i][j] = arr_90[i-3][j-9]

        elif s == 'L':
            tmp = []
            for i in range(0,9):
                tmp.append(cu[i][3])
            tmp.append(cu[5][11])
            tmp.append(cu[4][11])
            tmp.append(cu[3][11])

            cu[5][11] = tmp[0]
            cu[4][11] = tmp[1]
            cu[3][11] = tmp[2]

            cu[0][3] = tmp[3]
            cu[1][3] = tmp[4]
            cu[2][3] = tmp[5]

            cu[3][3] = tmp[6]
            cu[4][3] = tmp[7]
            cu[5][3] = tmp[8]

            cu[6][3] = tmp[9]
            cu[7][3] = tmp[10]
            cu[8][3] = tmp[11]
            
            # 왼쪽 -90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(0,3):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(3,6):
                for j in range(0,3):
                    cu[i][j] = arr_90[i-3][j]

        elif s == 'R':
            tmp = []
            for i in range(0,9):
                tmp.append(cu[i][5])
            tmp.append(cu[5][9])
            tmp.append(cu[4][9])
            tmp.append(cu[3][9])

            cu[3][5] = tmp[0]
            cu[4][5] = tmp[1]
            cu[5][5] = tmp[2]

            cu[6][5] = tmp[3]
            cu[7][5] = tmp[4]
            cu[8][5] = tmp[5]

            cu[5][9] = tmp[6]
            cu[4][9] = tmp[7]
            cu[3][9] = tmp[8]

            cu[0][5] = tmp[9]
            cu[1][5] = tmp[10]
            cu[2][5] = tmp[11]
            
            # 왼쪽 -90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(6,9):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr))[::-1]
            for i in range(3,6):
                for j in range(6,9):
                    cu[i][j] = arr_90[i-3][j-6]

    elif d == '+':
        if s == 'U':
            tmp = []
            for i in range(0,12):
                tmp.append(cu[3][i])
            cu[3][0] = tmp[3]
            cu[3][1] = tmp[4]
            cu[3][2] = tmp[5]

            cu[3][3] = tmp[6]
            cu[3][4] = tmp[7]
            cu[3][5] = tmp[8]

            cu[3][6] = tmp[9]
            cu[3][7] = tmp[10]
            cu[3][8] = tmp[11]

            cu[3][9] = tmp[0]
            cu[3][10] = tmp[1]
            cu[3][11] = tmp[2]
            
            # 왼쪽 +90도 회전
            arr = []
            for i in range(0,3):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(0,3):
                for j in range(3,6):
                    cu[i][j] = arr_90[i][j-3]

        elif s == 'D':
            tmp = []
            for i in range(0,12):
                tmp.append(cu[5][i])
            cu[5][3] = tmp[0]
            cu[5][4] = tmp[1]
            cu[5][5] = tmp[2]

            cu[5][6] = tmp[3]
            cu[5][7] = tmp[4]
            cu[5][8] = tmp[5]

            cu[5][9] = tmp[6]
            cu[5][10] = tmp[7]
            cu[5][11] = tmp[8]

            cu[5][0] = tmp[9]
            cu[5][1] = tmp[10]
            cu[5][2] = tmp[11]
            
            # 왼쪽 +90도 회전
            arr = []
            for i in range(6,9):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(6,9):
                for j in range(3,6):
                    cu[i][j] = arr_90[i-6][j-3]

        elif s == 'F':
            tmp = []
            for i in range(3,6):
                tmp.append(cu[i][2])

            for i in range(3,6):
                tmp.append(cu[6][i])
            tmp.append(cu[5][6])
            tmp.append(cu[4][6])
            tmp.append(cu[3][6])

            tmp.append(cu[2][5])
            tmp.append(cu[2][4])
            tmp.append(cu[2][3])

            cu[2][5] = tmp[0]
            cu[2][4] = tmp[1]
            cu[2][3] = tmp[2]

            cu[3][2] = tmp[3]
            cu[4][2] = tmp[4]
            cu[5][2] = tmp[5]

            cu[6][3] = tmp[6]
            cu[6][4] = tmp[7]
            cu[6][5] = tmp[8]

            cu[5][6] = tmp[9]
            cu[4][6] = tmp[10]
            cu[3][6] = tmp[11]

            # 왼쪽 +90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(3,6):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(3,6):
                for j in range(3,6):
                    cu[i][j] = arr_90[i-3][j-3]

        elif s == 'B':
            tmp = []
            for i in range(3,6):
                tmp.append(cu[i][0])

            for i in range(3,6):
                tmp.append(cu[8][i])

            tmp.append(cu[5][8])
            tmp.append(cu[4][8])
            tmp.append(cu[3][8])

            tmp.append(cu[0][5])
            tmp.append(cu[0][4])
            tmp.append(cu[0][3])

            cu[8][3] = tmp[0]
            cu[8][4] = tmp[1]
            cu[8][5] = tmp[2]

            cu[5][8] = tmp[3]
            cu[4][8] = tmp[4]
            cu[3][8] = tmp[5]

            cu[0][5] = tmp[6]
            cu[0][4] = tmp[7]
            cu[0][3] = tmp[8]

            cu[3][0] = tmp[9]
            cu[4][0] = tmp[10]
            cu[5][0] = tmp[11]

            # 왼쪽 +90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(9,12):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(3,6):
                for j in range(9,12):
                    cu[i][j] = arr_90[i-3][j-9]

        elif s == 'L':
            tmp = []
            for i in range(0,9):
                tmp.append(cu[i][3])
            tmp.append(cu[5][11])
            tmp.append(cu[4][11])
            tmp.append(cu[3][11])

            cu[3][3] = tmp[0]
            cu[4][3] = tmp[1]
            cu[5][3] = tmp[2]

            cu[6][3] = tmp[3]
            cu[7][3] = tmp[4]
            cu[8][3] = tmp[5]

            cu[5][11] = tmp[6]
            cu[4][11] = tmp[7]
            cu[3][11] = tmp[8]

            cu[0][3] = tmp[9]
            cu[1][3] = tmp[10]
            cu[2][3] = tmp[11]
            
            # 왼쪽 +90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(0,3):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(3,6):
                for j in range(0,3):
                    cu[i][j] = arr_90[i-3][j]

        elif s == 'R':
            tmp = []
            for i in range(0,9):
                tmp.append(cu[i][5])
            tmp.append(cu[5][9])
            tmp.append(cu[4][9])
            tmp.append(cu[3][9])

            cu[0][5] = tmp[3]
            cu[1][5] = tmp[4]
            cu[2][5] = tmp[5]

            cu[3][5] = tmp[6]
            cu[4][5] = tmp[7]
            cu[5][5] = tmp[8]

            cu[5][9] = tmp[0]
            cu[4][9] = tmp[1]
            cu[3][9] = tmp[2]

            cu[6][5] = tmp[9]
            cu[7][5] = tmp[10]
            cu[8][5] = tmp[11]
            
            # 왼쪽 +90도 회전
            arr = []
            for i in range(3,6):
                arr_tmp = []
                for j in range(6,9):
                    arr_tmp.append(cu[i][j])
                arr.append(arr_tmp)
            arr_90 = list(zip(*arr[::-1]))
            for i in range(3,6):
                for j in range(6,9):
                    cu[i][j] = arr_90[i-3][j-6]

for t in range(1,TC+1):
    n = int(input())
    qkdqjq = list(input())
    space = [[0,0,0,'w','w','w',0,0,0,0,0,0],[0,0,0,'w','w','w',0,0,0,0,0,0],[0,0,0,'w','w','w',0,0,0,0,0,0],
    ['g','g','g','r','r','r','b','b','b','o','o','o'],['g','g','g','r','r','r','b','b','b','o','o','o'],['g','g','g','r','r','r','b','b','b','o','o','o'],
    [0,0,0,'y','y','y',0,0,0,0,0,0],[0,0,0,'y','y','y',0,0,0,0,0,0],[0,0,0,'y','y','y',0,0,0,0,0,0]]
    for l in range(0,len(qkdqjq),+3):
        side = qkdqjq[l:l+2][0]
        dire = qkdqjq[l:l+2][1]
        change(side, dire, space)
    print(space[0][3],space[0][4],space[0][5], end = '', sep = '')
    print()
    print(space[1][3],space[1][4],space[1][5], end = '', sep = '')
    print()
    print(space[2][3],space[2][4],space[2][5], end = '', sep = '')
    print()