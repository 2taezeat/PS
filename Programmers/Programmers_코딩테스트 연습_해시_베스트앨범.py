from collections import defaultdict
def solution(genres, plays):
    dic1 = defaultdict(list)
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        dic1[g].append((p,i))
    answer = []
    for k,v in dic1.items():
        sum1 = 0
        for (a,j) in v:
            sum1 += a

        f = sorted(v, key = lambda x : (x[0], -x[1]))
        answer.append((sum1,f))
        
    result = []
    answer.sort(reverse=True)
    for a in answer:
        if len(a[1]) == 1:
            result.append(a[1][-1][1])
        else:
            result.append(a[1][-1][1])
            result.append(a[1][-2][1])

    return result

print(solution(["classic", "pop", "classic", "pop", "classic", "classic"],[400, 600, 150, 600, 500, 500]))