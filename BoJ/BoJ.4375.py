import sys
l1 = []
for i in range(1,10000):
    b = '1'*i
    l1.append(int(b))

try:
    while(1):
        n = int(sys.stdin.readline())
        a = 0
        p = 0
        for l in l1:
            if l % n == 0:
                p = 1
                a = str(l)
                break

        if p == 1:
            print(len(a))

        if p == 0:
            continue

except:
    exit()
