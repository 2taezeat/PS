import itertools
p = 1
while(p==1):
    l1 = list(map(int,input().split()))
    p = l1[0]
    if p ==0:
        break

    l1.pop(0)


    a = list(itertools.combinations(l1,6))
    for i in a:
        for j in i:
            print(j, end =' ')
        print()

    print()
    p = 1
