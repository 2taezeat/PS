N,M,K = map(int,input().split())
tree_space =  [[[] for j in range(N)] for i in range(N)]
d_plus = []
for i in range(N):
    d_plus.append(list(map(int,input().split())))
for i in range(M):
    x,y,z = map(int,input().split())
    tree_space[y-1][x-1].append(z)
didqns_space = [[5 for j in range(N)] for i in range(N)]
dy = [1,1,1,-1,-1,-1,0,0]
dx = [0,-1,1,0,1,-1,1,-1]

for year in range(K):
    # 봄
    dead_tree_list = []
    for i in range(N):
        for j in range(N):
            tree_list = tree_space[i][j]
            for t in range(len(tree_list)-1,-1,-1):
                
                if didqns_space[i][j] >= tree_list[t]:
                    didqns_space[i][j] -= tree_list[t]
                    tree_list[t] += 1
                else:
                    dead_year = tree_list.pop(t)
                    dead_tree_list.append((dead_year,i,j))

    # 여름
    for d in dead_tree_list:
        didqns_space[ d[1] ][ d[2] ] += d[0]//2
    
    # 가을
    for i in range(N):
        for j in range(N):
            tree_list = tree_space[i][j]
            for t in range(len(tree_list)-1,-1,-1):
                
                if tree_list[t] % 5 == 0:
                    for e in range(8):
                        ny = i + dy[e]
                        nx = j + dx[e]

                        if 0<= ny < N and 0<=nx < N:
                            tree_space[ny][nx].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            didqns_space[i][j] = d_plus[j][i] + didqns_space[i][j]
            
answer = 0
for i in range(N):
    for j in range(N):
        answer = answer + len(tree_space[i][j])

print(answer)