X = int(input())
flist = [64]

while sum(flist) >= X:
    a = min(flist)
    b = a // 2
    flist.remove(a)
    flist.append(b)
    
    if sum(flist) >= X:
        pass
    else:
        flist.append(b)

    if sum(flist) == X:
        break

if X == 64:
    print(1)
else:
    print(len(flist))