import math
n = int(input())
l = list(map(int,input().split()))
b, c = map(int,input().split())
answer = 0

for a in l:
    m = a - b
    if m >= 0:
        q = math.ceil(m / c)
    else:
        q = 0

    answer = q + answer

print(answer+n)