import  itertools
N = int(input())
a = list(map(int,input().split()))
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

print(link)
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
    print(al)

    if al == list(A):
        print(1111111111)

    bl = []
    qb = [B[0]]
    while(qb):
        beta = qb.pop()
        for i in link[beta]:
            if i in B and i not in bl:
                bl.append(i)
                qb.append(i)
    bl.sort()
    print(bl)
    if bl == list(B):
        print(2222222)


    



    
#checking((0,2,3),(1,4,5) )

checking ((0,), (1, 2, 3, 4, 5))