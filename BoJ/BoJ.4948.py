
while(1):
    N = int(input())
    if N == 0:
        break

    nl = [i for i in range(2,N*2+1)]
    l1 = [True] * (2*N+1)
    l1[1] = l1[0] = False

    for i in range(2, N*2+1):
        if l1[i] == True:
            p = i
        else:
            continue

        j = 2
        while(True):
            k = j * p
            j = j + 1
            
            if k > 2*N :
                break
            l1[k] = False 
    
    c = 0
    for i in range(N+1,2*N+1):
        if l1[i] == True:
            c = c + 1
    print(c)
