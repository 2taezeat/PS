def solution(jobs):
    delay = 0
    now = 0
    jb = sorted(jobs, key=lambda x: x[1])

    while jb:
        for i in range(0,len(jb)):
            if jb[i][0] <= now:
                now = now + jb[i][1]
                delay = delay + (now - jb[i][0])
                jb.pop(i)
                break
            
            if i == len(jb) - 1:
                now += 1

    return delay // len(jobs)




print(solution([[0, 3], [1, 9], [2, 6]]))