from collections import defaultdict
def solution(clothes):
    dict1 = defaultdict(list)
    for (a,b) in clothes:
        dict1[b].append(a)

    tmp = []
    for v in dict1.values():
        tmp.append(len(v)+1)

    answer = tmp[0]
    for t in range(1,len(tmp)):
        answer *= tmp[t]

    return answer - 1
        

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))