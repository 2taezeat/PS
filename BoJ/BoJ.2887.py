def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
############################################33
n = int(input())
space = []
parent = [0] * n
for i in range(n):
    parent[i] = i

xl, yl, zl = [], [], []
for i in range(n):
    x, y, z = list(map(int,input().split()))
    xl.append((x, i))
    yl.append((y, i))
    zl.append((z, i))
    
xl.sort()
yl.sort()
zl.sort()
edges = []

for i in range(n-1):
    edges.append( ( xl[i+1][0] - xl[i][0] ,xl[i][1], xl[i+1][1] ) )
    edges.append( ( yl[i+1][0] - yl[i][0] ,yl[i][1], yl[i+1][1] ) )
    edges.append( ( zl[i+1][0] - zl[i][0] ,zl[i][1], zl[i+1][1] ) )

edges.sort()

result = 0
for e in edges:
    c, a, b = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result = result + c
print(result)