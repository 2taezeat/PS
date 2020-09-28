from collections import deque
import sys
input = sys.stdin.readline # 이렇게 해야 시간 초과가 안뜸
n,m,k,x = map(int,input().split())
space = [ [] for i in range(n+1)]

# 0 번째 도시는 없음. index j이 j번째 도시를 의미함. 그래서 n이 아니라 n+1 임.
for i in range(m):
    a, b = map(int,input().split())

    space[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1]*(n+1)
distance[x] = 0 # 출발 도시까지으 거리는 0으로 설정 x -> x는 always 0.

q = deque()
q.append( x )

while q:
    now = q.popleft()
    for next_n in space[now]:

        # 아직 방문하지 않은 도시라면
        if distance[next_n] == -1:
            distance[next_n] = distance[now] + 1

            q.append(next_n)


check = False
for d in range(1,n+1):
    if distance[d] == k:
        print(d)
        check = True

if check == False:
    print(-1)