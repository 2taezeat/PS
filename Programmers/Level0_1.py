def solution(v):
    xl = []
    yl = []
    for i in range(3):
        xl.append(v[i][0])
        yl.append(v[i][1])

    xxl = []
    yyl = []
    for i in range(3):
        xxl.append( [xl[i], xl.count(xl[i])] )
        yyl.append( [yl[i], yl.count(yl[i])] )

    for i in range(3):
        if xxl[i][1] == 1:
            xanswer = xxl[i][0]
            break

    for i in range(3):
        if yyl[i][1] == 1:
            yanswer = yyl[i][0]
            break

    return [xanswer,yanswer]


