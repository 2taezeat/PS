for t in range(1,11):
    n = int(input())
    space = [[0]*(n+4) for i in range(255)]
    l = list(map(int,input().split()))

    for i in range(2,n+4): 
        for j in range(l[i-2]):

            space[j][i] = 1

        if i > n:
            break

    answer = 0
    for x in range(len(l)):
        for i in range(0,l[x]):
            
            if space[i][x] == 0 and space[i][x+1] == 0 and space[i][x+3] == 0 and space[i][x+4] == 0:
                answer = answer + 1

    print('#',t,' ',answer, sep='')
            
            