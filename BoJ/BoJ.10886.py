n = int(input())
c,d = 0,0
for i in range(n):
    a = int(input())

    if a == 1:
        c = c + 1
    else:
        d = d + 1


if c<d:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')