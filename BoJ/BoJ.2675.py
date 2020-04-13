t = int(input())

for i in range(t):
    l = input()
    r = l[0]
    s = l[2:]
    
    for j in s:
        print(int(r)*j,end='')

    print()