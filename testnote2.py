from itertools import permutations, combinations, product
import copy
def solution(n, weak, dist):
    dist.sort(reverse=True)
    #list1 = [i for i in range(1,n)] + [j for j in range(n,2*n)] # 원형 -> 2배 1차원 배열
    #weak = set(weak)
    for d in range(1,len(dist)+1):
        friend = dist[0:d]
        for p in permutations(weak,d):
            tmp_weak = copy.deepcopy(weak)
            set1 = set()
            qjadnp = []
            for i in range(len(p)):
                min1 = p[i]
                max1 = p[i] + friend[i]
            
                if max1 >= n:
                    qjadnp.append((min1,n-1))
                    qjadnp.append((0,max1 % n))

                else:
                    qjadnp.append((min1,max1))


            for m1, m2 in qjadnp:
                w = 0
                while(w < len(weak)):
                    if m1 <= tmp_weak[w] <= m2:
                        set1.add(tmp_weak[w])
#                        count += 1
#                        tmp_weak.remove(w)
                    w += 1

                if len(set1) == len(weak):
                    return d



            # count = 0
            # for i in range(len(p)):
            #     for j in range(friend[i]+1):
            #         k = (p[i] + j)

            #         if k > (2*n):
            #             break
                    
            #         if k % n in tmp_weak:
            #             tmp_weak.remove(k % n)
                    
            #         if len(tmp_weak) == 0:
            #             return d

            #         # try:
            #         #     tmp_weak.remove( k % n )
            #         # except:
            #         #     pass

            #         # if tmp_weak == []:
            #         #     return d

    return -1


print(solution (12, [1, 5, 6, 10], [1, 2, 3, 4])  )
#print(solution (12, [1, 3, 4, 9, 10], [3, 5, 7])  )