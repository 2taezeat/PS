import sys
T = int(input())

for i in range(T):
    s = input()
    l = len(s)
    p = 0
    for c in range(0,l//2):
        if s[c] != s[l-c-1]:
            p = 1
            break

    if p == 0:
        print(p)
    else:
        list1 = list(s)
        list2 = list(s)
        list1.pop(c)
        list2.pop(l-c-1)
        l1 = len(list1)
        
        p1,p2 = 1,1
        for c in range(0,l1//2):
            if list1[c] != list1[l1-c-1]:
                p1 = 2
                break
        

        for c in range(0,l1//2):
            if list2[c] != list2[l1-c-1]:
                p2 = 2
                break

        if p1 == 1 or p2 == 1:
            print(1)
        else:
            print(2)
