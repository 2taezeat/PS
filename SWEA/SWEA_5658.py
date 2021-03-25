from collections import deque
tc = int(input())
for t in range(tc):
    N, K = map(int,input().split())
    l1 = list(input())
    bar = N//4
    vktodehlstn = []

    for i in range(bar+1):
        if i == 0:
            for j in range(4):
                b = "".join(l1[ bar*j : j*bar+bar ])
                vktodehlstn.append(b)
        else:
            a = l1.pop()
            l1.insert(0,a)
            for j in range(4):
                b = "".join(l1[ bar*j : j*bar+bar ])
                vktodehlstn.append(b)


    vktodehlstn = list(set(vktodehlstn))
    vktodehlstn.sort(reverse=True)
    X = "0x" + vktodehlstn[K-1]
    h = int(X, 16)
    print("#",t+1,' ',h, sep='')
        
        