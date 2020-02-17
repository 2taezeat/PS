import math 
N, M = map(int,input().split())
al = list(map(int,input().split()))
l1 = [ (i+1) for i in range(N)]
sum1 = 0
for i in range(M):
    llen = len(l1)
    count2, count3 = 0, 0
    standard = math.ceil( llen / 2 )
    target1 = al[i]
    target = l1.index(target1)+1

    if target == 1:
        del l1[0]
    
    else:
        if target <= (standard):
            for k in range( target-1 ):
                count2 = count2 + 1
                move2 = l1[0]
                l1.append(move2)
                del l1[0]
            del l1[0]

        else:
            b = llen - target
            for x in range(b):
                move3 = l1[-1]
                l1.insert(0,move3)
                l1.pop()
                count3 = count3 + 1
            count3 = count3 + 1
            l1.pop()

    sum1 = sum1 + count2 + count3

print(sum1)