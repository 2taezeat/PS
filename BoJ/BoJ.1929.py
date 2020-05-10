result = []
M,N = map(int,input().split())
nl = [i for i in range(2,N+1)]
l1 = [True] * (N+1)
l1[1] = l1[0] = False

for i in range(2,N+1):
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

prime = []
for i in range(M,N+1):
    if l1[i] == True:
        print(i)

