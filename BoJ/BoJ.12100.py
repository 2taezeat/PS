import itertools, copy
n = int(input())
space = []
for i in range(n):
    space.append( list(map(int,input().split())) )
answerlist = []
p = [1,2,3,4]
prob = list(itertools.product(p, repeat=5))

for q in prob:
    newspace = copy.deepcopy(space)

    for d in q:
        l1 = []

        if d == 1:
            for i in range(n):
                arr = []
                for j in range(n):
                    if newspace[j][i] != 0:
                        arr.append(newspace[j][i])

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

                for r in range(n):
                    try:
                        newspace[r][L] = nl1[r]
                    except:
                        newspace[r][L] = 0

        if d == 2:
            for i in range(n):
                arr = []
                for j in range(n-1,-1,-1):
                    if newspace[j][i] != 0:
                        arr.append(newspace[j][i])

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

                for r in range(n):
                    try:
                        newspace[n-1-r][L] = nl1[r]
                    except:
                        newspace[n-1-r][L] = 0

        if d == 3:
            for i in range(n):
                arr = []
                for j in range(n):
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

                for r in range(n):
                    try:
                        newspace[L][r] = nl1[r]
                    except:
                        newspace[L][r] = 0
        
        if d == 4:
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
                    
                for r in range(n):
                    try:
                        newspace[L][n-1-r] = nl1[r]
                    except:
                        newspace[L][n-1-r] = 0

    answerlist.append( max(map(max, newspace)) )

print(max(answerlist))