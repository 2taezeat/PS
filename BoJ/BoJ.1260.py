import sys
from queue import Queue

def bfs(graph, start_node):
    q = Queue()
    q.put(start_node)
    visit = {}
    while q.qsize() > 0:
        node = q.get()
        if node not in visit:
            visit[node] = True
            sortedqlist = sorted(list(graph[node]))
            for nextNode in sortedqlist:
                q.put(nextNode)
            
    return visit

def dfs(graph, start_node):
    visit = {}
    stack = []  
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack = stack + sorted( list (graph[node] ), reverse = True)

    return visit

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph_list = [set([]) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph_list[i].add(j)
    graph_list[j].add(i)

rd = dfs(graph_list, V).keys()
for k in rd:
    print(k, end=' ')
print()
rb = bfs(graph_list,V)
for k in rb:
    print(k, end=' ')