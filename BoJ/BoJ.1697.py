import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int,input().split())

def op(n,i):
    if i == 0:
        return n - 1
    elif i == 1:
        return n + 1
    elif i == 2:
        return 2 * n

def bfs(graph, start):
    q = deque()    
    q.append(start)

    while q:
        node = q.popleft()
        if visit[K] != 0:
            return visit

        for i in range(3):
            new = op(node,i)

            if 0 <= new < 100001 and visit[new] == 0:
                q.append(new)
                visit[new] = 1 + visit[node]
                
    return visit

visit = [0] * 100001
if N == K:
    print(0)
else:
    a = bfs(visit,N)
    print(a[K])
