# l1 = [[1,2,7],[3,4,5]]

# print(max(map(max, l1)))
n = int(input())
newspace = []
for i in range(n):
    newspace.append( list(map(int,input().split())) )

l1 = []
for i in range(n):
    arr = []
    for j in range(n-1,-1,-1):
        if newspace[i][j] != 0:
            arr.append(newspace[i][j])

    l1.append(arr)
    

for L in range(len(l1)):
    l = l1[L]
    nl1 = []
    k = 0
    while(k < len(l)-1):
        if l[k] == l[k+1]:
            nl1.append(l[k]*2)
            k = k + 1
        else:
            nl1.append(l[k])
        k = k + 1

    try:
        nl1.append(l[k])
    except:
        pass
        
    print(nl1)

    for r in range(n):
        try:
            newspace[L][n-1-r] = nl1[r]
        except:
            newspace[L][n-1-r] = 0

print('-------------')
for i in range(n):
    print(newspace[i])