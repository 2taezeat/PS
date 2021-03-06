t = int(input())
for i in range(t):
    s = list(input())
    qa = 0
    qb = 0
    qc = 0

    for char in s:
        if char == 'a':
            qa = qa + 1
        elif char == 'b':
            qb = qb + 1
        elif char == 'c':
            qc = qc + 1

        if qa >= 1 and qb >= 1 and qc >= 1:
            qa = qa - 1
            qb = qb - 1
            qc = qc - 1

    if (qa + qb + qc) == 0 or (qa + qb + qc) == 1:
        print("#",i+1," YES", sep='')
        continue
    elif (qa == 0 and qb == 1 and qc == 1 ) or (qa == 1 and qb == 0 and qc == 1 ) or (qa == 1 and qb == 1 and qc == 0 ) :
        print("#",i+1," YES", sep='')
        continue

    print("#",i+1," NO", sep='')
