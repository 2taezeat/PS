l1 = list(input()) 
l2 = list(input())
l3 = list(input())
l4 = list(input())
l5 = list(input())

t1 = []
t2 = []
t3 = []
t4 = []

t1.append( l1[0:3] )
t1.append( l2[0:3] )
t1.append( l3[0:3] )
t1.append( l4[0:3] )
t1.append( l5[0:3] )

t2.append( l1[4:7] )
t2.append( l2[4:7] )
t2.append( l3[4:7] )
t2.append( l4[4:7] )
t2.append( l5[4:7] )

t3.append( l1[8:11] )
t3.append( l2[8:11] )
t3.append( l3[8:11] )
t3.append( l4[8:11] )
t3.append( l5[8:11] )

t4.append( l1[12:15] )
t4.append( l2[12:15] )
t4.append( l3[12:15] )
t4.append( l4[12:15] )
t4.append( l5[12:15] )

t = [t1,t2,t3,t4]
answer = []
for i in range(4):
    tl = t[i]
    if tl[1][1] == '.' and tl[2][1] == '.' and tl[3][1] == '.':
        a1 = 0
    elif tl[0][0] == '.' and tl[0][1] and tl[1][0] == '.' and tl[1][1] == '.' and tl[2][0] == '.' and tl[2][1] == '.' and tl[3][0] == '.' and tl[3][1] == '.' and tl[4][0] == '.' and tl[4][1] == '.':
        a1 = 1
    elif tl[3][1] == '.' and tl[3][2] == '.' and tl[1][1] == '.' and tl[1][0] == '.':
        a1 = 2
    elif tl[1][0] == '.' and tl[3][0] == '.' and tl[3][0] == '.' and tl[3][1] == '.':
        a1 = 3
    elif tl[0][1] == '.' and tl[1][1] == '.' and tl[3][1] == '.'and tl[4][1] == '.' and tl[4][0] == '.':
        a1 = 4
    elif tl[1][2] == '.' and tl[3][0] == '.' and tl[1][1] == '.' and tl[3][1] == '.':
        a1 = 5
    elif tl[1][2] == '.' and tl[1][1] == '.' and tl[3][1] == '.':
        a1 = 6
    elif tl[1][0] == '.' and tl[1][1] == '.' and tl[2][0] == '.' and tl[2][1] == '.' and tl[3][0] == '.' and tl[3][1] == '.' and tl[4][0] == '.' and tl[4][1] == '.':
        a1 = 7
    elif tl[1][1] == '.' and tl[3][1] == '.':
        a1 = 8
    elif tl[1][1] == '.' and tl[3][0] == '.' and tl[3][1] == '.':
        a1 = 9

    answer.append(a1)

print(answer[0],end='')
print(answer[1],end='')
print(":",end='')
print(answer[2],end='')
print(answer[3],end='')