import itertools
def solution(orders, course):
    orders_list = []
    result = []
    for o in orders:
        i = list(o)
        orders_list.append(i)

    for c in course:
        semi = []
        for ol in orders_list:
            if len(ol) >= c:
                comb = list( itertools.combinations(ol,c) )
            else:
                continue

            for cc in comb:
                cc = list(cc)
                cc.sort()
                nncc = ''.join(cc)
                semi.append(nncc)
        
        a = list(set(semi))
        dic1 = {string : 0 for string in a}

        for s in semi:
            dic1[s] += 1
        l_d = list(dic1.items())
        l_d.sort(key = lambda x : x[1], reverse = True)

        if l_d != []:
            stand = l_d[0][1]

            for k,v in l_d:
                if v == stand and v > 1:
                    result.append(k)
                else:
                    break

    result.sort()
    return result



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
