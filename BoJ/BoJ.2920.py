l1 = list(map(int,input().split()))
p = 0

for i in range(7):
    if l1[i] < l1[i+1]:
        p = p + 1
    else:
        p = p - 1

if p == 7:
    print('ascending')
elif p == -7:
    print('descending')
else:
    print('mixed')