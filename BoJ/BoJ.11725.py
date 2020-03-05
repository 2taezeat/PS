import sys
input = sys.stdin.readline

def dfs(graph, start_node,parent):
    stack = []  
    stack.append(start_node)

    while stack:
        node = stack.pop()

        for i in graph[node]:    
            parent[i].append(node)
            stack.append(i)
            graph[i].remove(node)

    return parent

N = int(input())
graph_list = [[] for _ in range(N+1)]
parent = [[] for _ in range(N + 1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    graph_list[i].append(j)
    graph_list[j].append(i)

a = dfs(graph_list,1,parent)
for i in a[2:]:
    print(i[0])