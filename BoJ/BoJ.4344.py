c = int(input())

for i in range(c):
    
    l1 = list(map(int,input().split()))
    aver = (sum(l1)-l1[0]) / l1[0]
    cl = []

    for st in range(1,len(l1)):
        if l1[st] > aver:
            cl.append(st)

    rate = len(cl) / (len(l1) -1 )
    rate = round(rate,5)
    rate = rate*100
    print('%.3f'% rate+'%')