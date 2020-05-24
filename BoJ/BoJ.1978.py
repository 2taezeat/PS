N = int(input())
l1 = list(map(int,input().split()))
c = N

for i in range(N):

    if l1[i] == 1 :
        c = c - 1
        
    else:
        for d in range(2,l1[i]):

            if l1[i] % d == 0:
                c = c - 1
                break

print(c)
