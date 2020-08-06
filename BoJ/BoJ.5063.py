n = int(input())

for i in range(n):
    r,e,c = map(int,input().split())

    if e > r + c:
        print("advertise")
    elif e < r + c:
        print("do not advertise")
    else:
        print("does not matter")