import bisect
l1 = [[] for i in range(10001)]
l2 = [[] for i in range(10001)]

def count_by_range(a,l,u):
    low = bisect.bisect_left(a,l)
    upp = bisect.bisect_right(a,u)
    return ( upp - low )

def solution(words, queries):
    answer = []

    for word in words:
        lew = len(word)
        l1[lew].append( word )
        l2[lew].append( word[::-1] )

    # 이진 탐색을 위해서 정렬
    for i in range(10001):
        l1[i].sort()
        l2[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하면서 처리
        leq = len(q)
        if q[0] != '?':
            r1 = q.replace("?", "a")
            r2 = q.replace("?", "z")
            result = count_by_range( l1[leq], r1, r2 )

        else:
            r3 = q[::-1].replace("?", "a")
            r4 = q[::-1].replace("?", "z")
            result = count_by_range(l2[leq], r3, r4)

        answer.append(result)

    return answer

r = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])
print(r)