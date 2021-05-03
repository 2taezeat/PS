def solution(N, stages):
    l1,result = [0 for _ in range(N+2)], []
    for i in stages: l1[i] = l1[i] + 1
    for i in range(1,len(l1)-1):
        sum1 = sum(l1[i:len(l1)+1])
        if sum1 == 0: result.append((0,i)) # divide by zero 처리
        else: result.append( ( l1[i] / sum(l1[i:len(l1)+1]), i))
    result.sort(key = lambda x : (-x[0], x[1]))
    
    return [b for (a,b) in result]


print(solution(1,[1]))

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print('------------------------')
print(solution(4,[4,4,4,4,4]))