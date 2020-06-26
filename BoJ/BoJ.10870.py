def fb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fb(n-1) + fb(n-2)

print( fb( int(input()) ))