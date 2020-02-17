def gcd(a,b):
    if a < b:
        (a,b) = (b,a)
    while b != 0:
        (a,b) = (b,a%b)
    return a

N = int(input())
number =[]
for k in range(N):
    k = int(input())
    number.append(k)

number.sort()

a = []

for i in range(N-1):
    b = number[i+1] - number[i]
    a.append(b)

if N == 2:
    g1 = a[0]
    for h in range(2,g1+1):
        if g1%h == 0 :
            print(h,end=' ')

else:
    g1 = gcd(a[0],a[1])


    for j in range(2,N-1):
        g1 = gcd(g1,a[j])

    for h in range(2,g1+1):
        if g1%h == 0 :
            print(h,end=' ')
