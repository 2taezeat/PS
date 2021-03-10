l = []
l.append(list(input()))
l.append(list(input()))
l.append(list(input()))
l.append(list(input()))
k = int(input())
arr = []
answer = 0
for i in range(k):
    n, d = map(int,input().split())
    arr.append([n,d])

for i in range(k):
    N, D = arr[i][0], arr[i][1]
    move = [[N,D]]

    ########## Check
    if N == 1:
        if ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([2,-D])
            move.append([3,D])
            move.append([4,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([2,-D])
            move.append([3,D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([2,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([2,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass

    elif N == 2:
        N = N - 1
        if ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([1,-D])
            move.append([3,-D])
            move.append([4,D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([1,-D])
            move.append([3,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([1,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([1,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([3,-D])
            move.append([4,D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([3,-D])

    elif N == 3:
        N = N - 2
        if ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([1,D])
            move.append([2,-D])
            move.append([4,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([1,D])
            move.append([2,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([4,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([2,-D])
            move.append([4,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([4,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            move.append([2,-D])

    elif N == 4:
        N = N - 3
        if ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([1,-D])
            move.append([2,D])
            move.append([3,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([3,-D])
        elif ( l[N-1][2] != l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([2,D])
            move.append([3,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] == l[N+1][6] ) and ( l[N+1][2] != l[N+2][6] ) :
            move.append([3,-D])
        elif ( l[N-1][2] == l[N][6] ) and ( l[N][2] != l[N+1][6] ) and ( l[N+1][2] == l[N+2][6] ) :
            pass

    ## Rotate
    for m in move:
        nn = m[0]
        dd = m[1]

        if nn == 1:
            if dd == 1:
                v = l[ nn-1 ].pop()
                l[ nn-1 ].insert(0,v)
            if dd == -1:
                v = l[ nn-1 ].pop(0)
                l[ nn-1 ].append(v)

        if nn == 2:
            if dd == 1:
                v = l[ nn-1 ].pop()
                l[ nn-1 ].insert(0,v)
            if dd == -1:
                v = l[ nn-1 ].pop(0)
                l[ nn-1 ].append(v)

        if nn == 3:
            if dd == 1:
                v = l[ nn-1 ].pop()
                l[ nn-1 ].insert(0,v)
            if dd == -1:
                v = l[ nn-1 ].pop(0)
                l[ nn-1 ].append(v)

        if nn == 4:
            if dd == 1:
                v = l[ nn-1 ].pop()
                l[ nn-1 ].insert(0,v)
            if dd == -1:
                v = l[ nn-1 ].pop(0)
                l[ nn-1 ].append(v)

if l[0][0] == '1':
    answer = answer + 1
if l[1][0] == '1':
    answer = answer + 2
if l[2][0] == '1':
    answer = answer + 4
if l[3][0] == '1':
    answer = answer + 8

print(answer)