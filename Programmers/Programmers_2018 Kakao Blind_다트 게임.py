import re
def solution(dartResult):
    l1 = []
    d = 0
    while (d <len(dartResult)):
        if 48 <= ord(dartResult[d]) <= 57 :
            if (dartResult[d+1]) == '0':
                l1.append([10])
                d = d + 2
                continue
            else:
                l1.append([int(dartResult[d])])
        else:
            d = d + 1
            continue

        d = d + 1

    a = re.split('[0-9]',dartResult)
    aa = []
    for i in range(len(a)):
        if a[i] != '':
            aa.append(a[i])
        
    for i in range(len(aa)):
        if aa[i] == '':
            continue

        for c in aa[i]:
            l1[i].append(c)

        if len(l1[i]) == 2:
            l1[i].append('-')
    
    a1 = l1[0][0]
    a2 = l1[0][1]
    a3 = l1[0][2]
    r1 = 0
    r2 = 0
    r3 = 0
    if a2 == 'S':
        r1 = a1 ** 1
    elif a2 == 'D':
        r1 = a1 ** 2
    elif a2 == 'T':
        r1 = a1 ** 3

    if a3 == '*':
        r1 = (r1*2)
    elif a3 == '#':
        r1 = r1*(-1)

    a1 = l1[1][0]
    a2 = l1[1][1]
    a3 = l1[1][2]

    if a2 == 'S':
        r2 = a1 ** 1
    elif a2 == 'D':
        r2 = a1 ** 2
    elif a2 == 'T':
        r2 = a1 ** 3

    if a3 == '*':
        r2 = (r2*2)
        r1 = (r1*2)
    elif a3 == '#':
        r2 = r2*(-1)

    a1 = l1[2][0]
    a2 = l1[2][1]
    a3 = l1[2][2]

    if a2 == 'S':
        r3 = a1 ** 1
    elif a2 == 'D':
        r3 = a1 ** 2
    elif a2 == 'T':
        r3 = a1 ** 3

    if a3 == '*':
        r3 = (r3*2)
        r2 = (r2*2)
    elif a3 == '#':
        r3 = r3*(-1)

    return r1+r2+r3


#print(solution('1D2S#10S'))
print(solution('1D2S3T*'))