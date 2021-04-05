import  itertools
N = int(input())
peo = list(map(int,input().split()))
l0 = [i for i in range(0,N)]
result = []
gnqh = []
for i in range(1,(N//2)+1):
    a = list(itertools.combinations(l0,i))
    b = list(itertools.combinations(l0,N-i))[::-1]
    c = list(zip(a,b))
    gnqh.append(c)
link = []
for i in range(N):
    k = list(map(int,input().split()))
    for j in range(len(k)):
        k[j] = k[j] - 1
    link.append(k[1:])

def checking(A,B):
    al = [A[0]]
    qa = [A[0]]
    while(qa):
        alpha = qa.pop()
        for i in link[alpha]:
            if i in A and i not in al:
                al.append(i)
                qa.append(i)
    al.sort()
    if al != list(A):
        return False

    bl = [B[0]]
    qb = [B[0]]
    while(qb):
        beta = qb.pop()
        for i in link[beta]:
            if i in B and i not in bl:
                bl.append(i)
                qb.append(i)
    bl.sort()
    if bl != list(B):
        return False

    return True

for ggg in gnqh:
    for gg in ggg:
        
        if checking(gg[0],gg[1]) == True:
            asum = 0
            bsum = 0
            for a in gg[0]:
                asum = asum + peo[a]
            for b in gg[1]:
                bsum = bsum + peo[b]

            result.append(abs( asum - bsum ))

if result == []:
    print(-1)
else:
    print(min(result))