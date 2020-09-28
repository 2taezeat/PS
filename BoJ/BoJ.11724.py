import sys
from collections import deque
sys.setrecursionlimit(10000) # 파이썬 재귀제한 해제
input = sys.stdin.readline # 시간 초과를 방지하기 위함.
# input 받고, 변수 초기화
n,m = map(int,input().split())
result = 0
graph = [ [] for i in range(n)] 
visited = [False] * (n) # 방문한 노드를 체크 함. True 값이면 방문했다는 의미임.

for i in range(m):
    a, b = map(int,input().split())
    # 1부터 시작함으로 -1을 한다. 무방향 그래프 임으로, a,b를 서로 swap 한 것도 추가한다.
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def dfs(node,g):
    visited[node] = True
    for adj in g[node]: # 연결된 노드 : adj
        if not visited[adj]: # adj 노드가 방문된 노드가 아니라면
            dfs(adj,g)

for i in range(n): # 1,2,3,4,5.... 노드순으로 방문
    if not visited[i]: # 방문한 노드가 아니라면

        dfs(i,graph)
        result = result + 1

print(result)
