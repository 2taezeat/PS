n = 15
nb = format(n, 'b')

cnb = nb.count('1')

m = n + 1
while(1):
    
    c = 0
    bm = format(m, 'b')
    
    for b in bm:
        if b == '1':
            c = c + 1

    if cnb == c:
        break

    m = m + 1

print(m)