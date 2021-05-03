def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    tnsdnl = 0
    zero_count = 0

    for i in range(len(lottos)):
        if lottos[i] == 0: zero_count+=1
        elif lottos[i] in win_nums : tnsdnl += 1

    mx = 7 - (zero_count+tnsdnl)
    mi = 7 - tnsdnl
    
    if mi >= 6:
        mi = 6

    if mx >= 6:
        mx = 6

    answer = [mx,mi]
    return answer




#print(solution([0, 0, 0, 0, 0, 0],[31, 10, 45, 1, 6, 19]))

print(solution([1,2,3,4,5],[6,7,8,9,10]))