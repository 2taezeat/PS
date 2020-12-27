n = int(input())
distance = [[0]*(n) for _ in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))


for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):

        if i == n-1 and j == n-1:
            distance[i][j] = graph[0][0]

        elif i == n-1 and j !=n-1:
            distance[i][j] = distance[i][j-1] + graph[i][j]

        elif i != n-1 and j == n-1:
            distance[i][j] = distance[i-1][j] + graph[i][j]

        else:
            distance[i][j] = min(distance[i-1][j], distance[i][j-1] ) + graph[i][j]
            # try:
            #     distance[i][j] = min(distance[i-1][j], distance[i][j-1], distance[i][j+1] ) + graph[i][j]
            # except:
            #     distance[i][j] = min(distance[i-1][j], distance[i][j-1] ) + graph[i][j]


        print(i,j)


print(distance)