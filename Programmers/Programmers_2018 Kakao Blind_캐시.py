from collections import deque
def solution(cacheSize, cities):
    q = deque()
    t = 0
    if cacheSize == 0:
        return 5*len(cities)

    for c in cities:
        c = c.lower()
        if c in q:
            t = t + 1
            q.remove(c)
            q.append(c)

        else:
            if len(q) < cacheSize :
                q.append(c)
            else:
                q.popleft()
                q.append(c)
            t = t + 5

    return t


#print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#print(solution(1,	["Jeju", "Pangyo", "NewYork", "newyork"]))
#print(solution(0,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))