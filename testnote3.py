from itertools import permutations, combinations, product
import copy
def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak_double = weak + [i+12 for i in weak]

    for d in range(1,len(dist)+1):
        friend = dist[0:d]
        for p in permutations(weak,d):
            check = [False for _ in range(len(weak_double)) ]
            for i in range(len(p)):
                start = p[i]
                end = friend[i] + p[i]

                for w in range(len(weak_double)):
                    if start <= weak_double[w] <= end:
                        check[w] = True

                tmp = set()
                for j in range(len(check)):
                    if check[j]:
                        tmp.add(j % n)

                if len(tmp) == len(weak):
                    return d                      

    return -1


#print(solution (12, [1, 5, 6, 10], [1, 2, 3, 4])  )
print(solution (12, [1, 3, 4, 9, 10], [3, 5, 7])  )