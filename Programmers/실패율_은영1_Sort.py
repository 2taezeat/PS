from bisect import bisect_left, bisect_right
def solution(N, stages):
    
    dic = dict()
    s_sorted = sorted(stages)
    
    for i in range(N):
        left_idx = bisect_left(s_sorted, i + 1)
        right_idx = bisect_right(s_sorted, i + 1)
        if(len(s_sorted[left_idx:])):
            dic[i+1] = (right_idx - left_idx) / len(s_sorted[left_idx:])
        else:
            dic[i+1] = 0
        
    answer = [x[0] for x in sorted(dic.items(), key = lambda x: x[1], reverse = True)]
    return answer