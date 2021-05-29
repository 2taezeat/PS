def solution(n, results):
    win = {x:set() for x in range(1, n+1)}
    lose = {x:set() for x in range(1, n+1)}
    answer = 0
    for (w,l) in results:
        win[w].add(l)
        lose[l].add(w)

    for i in range(1,n+1):
        # 1에게 진 사람은 1이 진 사람들에게도 진다
        for l in win[i]:
            lose[l].update(lose[i])

        # 1에게 이긴 사람은 1한테 진 사람들에게 이긴다
        for w in lose[i]:
            win[w].update(win[i])

    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1


    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))