a, b, c = map(int,input().split())
set1 = {a,b,c}
l1 = [a,b,c]
set2 = list(set1)


if len(set2) == 1:
    print(10000 + a*1000)
elif len(set2) == 2:
    if l1[0] == l1[1]:
        print(1000+l1[0]*100)
    elif l1[0] == l1[2]:
        print(1000+l1[0]*100)
    else:
        print(1000+l1[1]*100)
elif len(set2) == 3:
    print(100*max(l1))