def solution(arr):
    N = len(arr)
    n = len(arr)
    B,o,z = 0,0,0
    while(n > 0):
        n = n // 2
        B += 1
    B = B - 1
    zero_change = 0
    one_change = 0
    for i in range(0,N,):
        for j in range(0,N):
            if arr[i][j] == 1:
                o += 1
            else:
                z += 1

    for b in range(B,0,-1):
        for i in range(0,N,2**b):
            for j in range(0,N,2**b):
                whkvy = []
                sta = arr[i][j]
                flag = True

                for y in range(i,i+2**b):
                    for x in range(j,j+2**b):
                        if arr[y][x] != sta or sta == 3 or sta == 4:
                            flag = False
                            break
                        
                        whkvy.append((y,x))

                    if flag == False:
                        break

                if sta == 0 and flag:
                    for (bb,aa) in whkvy:
                        zero_change += 1
                        arr[bb][aa] = 3
                    zero_change -=1

                elif sta == 1 and flag:
                    for (bb,aa) in whkvy:
                        one_change +=1
                        arr[bb][aa] = 4
                    one_change -=1

    return [z-zero_change,o-one_change]



#print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

