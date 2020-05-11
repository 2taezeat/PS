t = int(input())
l1 = []

for i in range(t):
    a, b = map(int,input().split())
    l1.append([a,b])

l1.sort()

for x,y in l1:
    print(x,y)
