import heapq
def solution(operations):
    h1 = [] ## 최대 힙
    h2 = [] ## 최소 힙
    for o in operations:
        if o[0] == 'I':
            item = int(o[2:])
            heapq.heappush(h1,(-item, item))
            heapq.heappush(h2,(item, item))

        elif o[-1] == '1' and o[-2] == ' ':
            if h1 == []:
                continue
            v = heapq.heappop(h1)[1]
            h2.remove((v,v))

        elif o[-2] == '-':
            if h1 == []:
                continue
            v = heapq.heappop(h2)[1]
            h1.remove((-v,v))

    if h1 == []:
        return [0,0]

    return [h1[0][1],h2[0][1]]
