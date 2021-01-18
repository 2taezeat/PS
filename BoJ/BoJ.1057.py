import math
N, a, b = map(int,input().split())
Round = 1
rc = math.ceil(math.log2(N))
list1 = [ y for y in range(N)]
k = N
a = a -1
b = b -1
for i in range( rc - 1):
    list1 = []
    
    if a % 2 ==0:
        if a - b == -1:
            break
    if a % 2 ==1:
        if a - b == +1:
            break 

    Round = Round + 1
    if ( k ) % 2 == 1: # 리스트 길이가 홀수
        for j in range( (k // 2) + 1 ):
            list1.append(j)
        a = a // 2
        b = b // 2
        k = len(list1)

    else:
        for j in range( k // 2 ):
            list1.append(j)
        k = len(list1)
        a = a // 2
        b = b // 2

    if a % 2 ==0:
        if a - b == -1:
            break
    if a % 2 ==1:
        if a - b == +1:
            break

if N == 2:
    print(1)
else:
    print(Round)