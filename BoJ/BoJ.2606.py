import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph_list = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    graph_list[i].append(j)
    graph_list[j].append(i)

def dfs(graph, start_node):
    visit = {}
    stack = []  
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack = stack + sorted( list (graph[node] ) )

    return visit


print(len(dfs(graph_list,1))-1)