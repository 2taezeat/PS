def solution(gems):
    set_gem = set(gems)
    length = len(set_gem)
    gnqh = []
    dict1 = dict()
    for i in range(len(gems)):
        try:
            del dict1[gems[i]]
        except:
            pass

        dict1[gems[i]] = i

        #print(dict1)

        if len(dict1) == length:
            vl2 = dict1.values()
            a = min(vl2)
            b = max(vl2)

            # vl = list(dict1.values())
            gnqh.append([b-a, a+1, b+1])
    

    gnqh.sort()
    return gnqh[0][1], gnqh[0][2]


print( solution(["DIA", "RUBY", "RUBY", "RUBY", "RUBY", "EMERALD", "SAPPHIRE", "DIA"]) )
print( solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) )
# print( solution(["AA", "AB", "AC", "AA", "AC"]) )
# print( solution(["XYZ", "XYZ", "XYZ"]) )
# print( solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) )