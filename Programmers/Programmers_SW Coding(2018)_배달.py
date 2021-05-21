# 플로이드 워셜 알고리즘
def solution(n, road, K):
    INF = int(1e7) # 무한을 의미하는 값으로 10억을 설정

    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for i in range(len(road)):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = road[i]
        graph[a][b] = min (c, graph[a][b]) 
        graph[b][a] = min (c, graph[b][a])

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for A in range(1, n + 1):
            for B in range(1, n + 1):
                graph[A][B] = min(graph[A][B], graph[A][k] + graph[k][B])

    answer = 0
    l1 = graph[1]
    for i in l1:
        if i <= K:
            answer += 1

    return answer

print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))