
def solution(n, computers):
    answer = []
    visit = [False for _ in range(n)]
    for i in range(n):        
        if visit[i] == False:
            visit[i] = True
            result = [i]
            q = [i]

            while q:
                t = q.pop()
                list1 = computers[t]
            
                for j in range(n):
                    if list1[j] == 1 and visit[j] == False:
                        result.append(j)
                        q.append(j)
                        visit[j] = True
                        
            answer.append(result)

    return len(answer)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))