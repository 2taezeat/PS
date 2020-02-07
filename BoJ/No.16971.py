N,M = map(int,input().split())
list1 = []
rowlist = []
columnlist = []
for i in range(N):
    l = list(map(int, input().split()))
    list1.append(l)

for i in range(N):
    rowsum = 0
    for j in range(M):
        if j == 0 or j == M-1 :
            rowsum = rowsum + list1[i][j]
        else:
            rowsum = rowsum + (list1[i][j]*2)
    rowlist.append(rowsum)
    
for i in range(M):
    columnsum = 0
    for j in range(N):
        if j == 0 or j == N-1 :
            columnsum = columnsum + list1[j][i]
        else:
            columnsum = columnsum + (list1[j][i]*2)
    columnlist.append(columnsum)

if N == 2 or M == 2:
    if N == 2 and M == 2:
        print(list1[0][0] + list1[0][1] + list1[1][0] + list1[1][1])
    else:
        if N == 2:
            maxcolumn = columnlist[0]
            columnsecond = columnlist[-1]
            if maxcolumn < columnlist[-1]:
                maxcolumn, columnsecond = columnlist[-1], columnlist[0]
            c0 = columnlist.pop(0)
            cl = columnlist.pop(M-2)
            mincolumn = min(columnlist)
            dcolumn = maxcolumn - mincolumn

            if dcolumn <= 0:
                result = sum(columnlist)*2 + columnsecond + maxcolumn
                print(result)
            else:
                columnlist.remove(mincolumn)
                result = sum(columnlist)*2 +( maxcolumn *2 ) + mincolumn + columnsecond
                print(result)

        if M == 2:
            maxrow = rowlist[0]
            rowsecond = rowlist[-1]
            if maxrow < rowlist[-1]:
                maxrow, rowsecond = rowlist[-1], rowlist[0]
            
            r0 = rowlist.pop(0)
            rl = rowlist.pop(N-2)
            minrow = min(rowlist)
            drow = maxrow - minrow

            if drow <= 0:
                result = sum(rowlist)*2 + rowsecond + maxrow
                print(result)
            else:
                rowlist.remove(minrow)
                result = sum(rowlist)*2 +( maxrow *2 ) + minrow + rowsecond
                print(result)

else:
    maxrow = rowlist[0]
    maxcolumn = columnlist[0]
    rowsecond = rowlist[-1]
    columnsecond = columnlist[-1]
    if maxrow < rowlist[-1]:
        maxrow, rowsecond = rowlist[-1], rowlist[0]
    if maxcolumn < columnlist[-1]:
        maxcolumn, columnsecond = columnlist[-1], columnlist[0]

    r0 = rowlist.pop(0)
    c0 = columnlist.pop(0)
    rl = rowlist.pop(N-2)
    cl = columnlist.pop(M-2)
    minrow = min(rowlist)
    mincolumn = min(columnlist)
    drow = maxrow - minrow
    dcolumn = maxcolumn - mincolumn

    if drow <= 0 and dcolumn <= 0: # 바꾸면 안되는 경우 
        result = sum(rowlist)*2 + rowsecond + maxrow

    else:
        if drow >= dcolumn : # row로 더하는 경우
            rowlist.remove(minrow)
            result = sum(rowlist)*2 +( maxrow *2 ) + minrow + rowsecond

        else: # colum으로 더하는 경우
            columnlist.remove(mincolumn)
            result = sum(columnlist)*2 +( maxcolumn *2 ) + mincolumn + columnsecond

    print(result)