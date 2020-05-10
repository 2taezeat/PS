result = []
M,N = map(int,input().split())
nl = [i for i in range(2,N+1)]
l1 = [True for i in range(N+1)]


for i in range(2,M+1):
    if l1[i] == True:
        p = i
    else:
        continue

    j = 2
    while(True):
        k = j * p
        j = j + 1

        if k > N:
            break
        l1[k] = False 

for i in range(M,len(l1)):
    if i ==0 or i ==1 :
        continue

    if l1[i] == True:
        print(i)