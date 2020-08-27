n = int(input())
c = 0

if (n == 1) or (n == 3):
    print(-1)
else:
    while(1):
        q = n // 5
        r = n % 5

        if r != 0:
            n = n - 2
            c = c + 1
        else:
            c = c + q
            break
        
        if n < 0:
            break

    print(c)