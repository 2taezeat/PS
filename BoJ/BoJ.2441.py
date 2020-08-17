n = int(input())

for i in range(0,n):

    for j in range(0,i):
        print(' ', end='')

    for k in range(n-i,0,-1):
        print('*', end='')

    print()