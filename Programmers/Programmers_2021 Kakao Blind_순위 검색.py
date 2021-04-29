import itertools, re
from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(info, query):
    result = []
    d = defaultdict(list)
    pro = list ( itertools.product([1,0], repeat=4))
    for i in range(len(info)):        
        aa = info[i].split(' ')
        for (t0,t1,t2,t3) in pro:
            if t0 == 0:
                l = '-'
            else:
                l = aa[0]
            if t1 == 0:
                j = '-'
            else:
                j = aa[1]
            if t2 == 0:
                c = '-'
            else:
                c = aa[2]
            if t3 == 0:
                f = '-'
            else:
                f = aa[3]
            d[l+j+c+f].append( int(aa[4]) )
        
    for i in range(len(query)):
        bb = re.split(' |and',query[i])
        l = bb[0]
        j = bb[3]
        c = bb[6]
        f = bb[9]
        s = int(bb[10])
        standard = l+j+c+f
        score_list = d[standard]
        if score_list == []:
            result.append(0)
        else:
            score_list.sort()
            a = bisect_left(score_list, s)
            result.append(len(score_list)-a)
            
    return result


print(solution( ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]))