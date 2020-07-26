h, m = map(int,input().split())

if 45<= m < 60:
    m = m - 45
else:
    h = h - 1
    m = m + 60 - 45

if h < 0:
    h = h + 24

print(h,m)