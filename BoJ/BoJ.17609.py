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


    print('c',c)

    s1= s.pop(c)

    print(s1)
        

############# 미 성공