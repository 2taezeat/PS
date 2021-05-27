def solution(citations):
    l1 = []
    mav = max(citations)

    for stand in range(0,mav+1):
        cnt = 0
        for c in citations:
            if c >= stand:
                cnt += 1

        if cnt >= stand:
            l1.append((stand,cnt))

    l1.sort(reverse=True)

    return l1[0][0]
    

#print(solution([3,0,6,1,5]))
print(solution([5,5,5,5]))