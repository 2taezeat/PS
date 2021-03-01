t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    bi = list(reversed(bin(m)))
    #print(bi)
    for j in range(len(bi)-1):

        if j >= n:
            print("#",i+1," ON", sep='')
            break

        if bi[j] == '0':
            #print("#",i," OFF", sep='')
            break

    if j < n:
        print("#",i+1," OFF", sep='')
        