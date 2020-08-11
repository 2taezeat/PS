import sys
n = int(sys.stdin.readline())
A,B,C,D = [],[],[],[]
for i in range(n):
    a,b,c,d = map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

d_ab, d_cd  = {}, {}

for e_a in A:
    for e_b in B:
        sumab = e_a + e_b
        if (d_ab.get(sumab)):
            d_ab[sumab] = d_ab[sumab] + 1 
        else:
            d_ab[sumab] = 1
    
for e_c in C:
    for e_d in D:
        sumcd = e_c + e_d
        if (d_cd.get(sumcd)):
            d_cd[sumcd] = d_cd[sumcd] + 1 
        else:
            d_cd[sumcd] = 1

count = 0
for _, sumkey in enumerate(d_ab):
    find = -(sumkey)
    if d_cd.get(find):
        count = count + (d_ab[-find] * d_cd[find])

print(count)