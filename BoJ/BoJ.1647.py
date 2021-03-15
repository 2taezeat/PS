# 도시 분할 계획 // ch10. 그래프 이론
def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
###########################
n, m = map(int,input().split())
parent = [0] * (n+1) 
edges = []
answer = 0
for i in range(1,n+1):
    parent[i] = i

for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()
l = 0
for e in edges:
    cost, a, b = e

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer = answer + cost
        l = cost

print(answer - l)

