t = int(input())
l1 = []
for i in range(t):
    k = input()
    sum1 = 0
    for c in k:
        try:
            if -1 < int(c) < 10:
                sum1 = sum1 + int(c)
        except:
            pass
    
    l1.append([k,len(k),sum1])

l1 = sorted(l1, key = lambda x : (x[1], x[2], x[0]) )

for i in range(t):
    print(l1[i][0])