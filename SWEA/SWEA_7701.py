t = int(input())

for i in range(t):
    n = int(input())

    l1 = set()
    for j in range(n):
        c = input()
        l1.add((c,len(c)))

    print("#",end='')
    print(i+1)
    
    l1 = list(l1)
    l1.sort(key = lambda x :(x[1],x[0]))
    
    for e in l1:
        print(e[0])
