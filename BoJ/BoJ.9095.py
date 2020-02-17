T = int(input())
alist = [1,2,4]
for i in range(3, 11):
    result = 0
    alist.append ( alist[i-1] + alist[i-2] + alist[i-3] )

for n in range(T):
    n = int(input())
    print(alist[n-1])

