for t in range(1,11):
    n = int(input())
    space = []
    for j in range(8):
        s = list(input())
        space.append(s)
    count = 0
################### 가로
    for i in range(0,8):
        for j in range(0,9-n):
            pal = ''

            for len1 in range(n):
                pal = pal + space[i][j+len1]

            if pal == pal[::-1]:
                count = count + 1
################## 세로
    for i in range(0,9-n):
        for j in range(0,8):
            pal = ''

            for len1 in range(n):
                pal = pal + space[i+len1][j]            

            if pal == pal[::-1]:
                count = count + 1

################### 출력
    print('#',end='')
    print( '{0} {1}'.format( t, count ) ) 