import copy
s = list(input())
l1,l2,l4 = [],[],[]

for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        l1.append([i,j+1])

for i in range(len(l1)):
    cs = s.copy()
    cs.insert(l1[i][0],'/')
    cs.insert(l1[i][1],'/')

    js = ''.join(cs)
    ljs = js.split('/')
    l2.append(ljs)

    l3 = []
    for t in ljs:
        nt = ''.join(list(reversed(t)))
        l3.append(nt)

    l4.append(l3)

l5 = []

for i in range(len(l4)):
    l5.append(''.join(l4[i]))


print(min(l5))