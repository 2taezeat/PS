def solution(N, stages):
    answer, r, pl = [], [], []
    l2 = [ 0 for i in range(N)]

    for i in range(N):
        pl.append(i)
        l2[pl[i]] = stages.count(pl[i]+1)
        b = 0
        for j in range(len(stages)):
            if pl[i]+1 <= stages[j]:
                b = b + 1
        
        if l2[i] == 0 or b == 0:
            answer.append([0,i+1])
        else:
            answer.append([ l2[i] / b ,i+1])        

    answer.sort(key = lambda x : x[0], reverse=True)

    for i in range(N):
        r.append(answer[i][1])

    return r

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print('------------------------')
print(solution(4,[4,4,4,4,4]))