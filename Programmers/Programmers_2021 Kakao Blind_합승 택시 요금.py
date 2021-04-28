def solution(n, s, a, b, fares):
    cost = [[999999999] * (n+1) for _ in range(n+1)]
    for A in range(1,n+1):
        for B in range(1,n+1):
            if A == B:
                cost[A][B] = 0

    for i in range(len(fares)):
        A,B, C = fares[i][0],fares[i][1],fares[i][2]
        cost[A][B] = C
        cost[B][A] = C

    for k in range(1,n+1):
        for A in range(1,n+1):
            for B in range(A,n+1):
                m = min(cost[A][B], cost[A][k] + cost[k][B])
                cost[A][B] = m
                cost[B][A] = m

    answer = 999999999
    for t in range(1,n+1):        
        total_cost = cost[s][t] + cost[t][a] + cost[t][b]
        answer = min(answer,total_cost)

    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))