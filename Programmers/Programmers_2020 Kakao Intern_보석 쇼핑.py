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

        if len(dict1) == length:
            vl = list(dict1.values())
            if vl[-1] == vl[0]:
                return vl[0]+1, vl[-1]+1
            else:
                gnqh.append([vl[-1]-vl[0], vl[0]+1, vl[-1]+1])
    
    gnqh.sort()
    return gnqh[0][1], gnqh[0][2]




print( solution(["DIA", "RUBY", "RUBY", "RUBY", "RUBY", "EMERALD", "SAPPHIRE", "DIA"]) )
print( solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) )
# print( solution(["AA", "AB", "AC", "AA", "AC"]) )
# print( solution(["XYZ", "XYZ", "XYZ"]) )
# print( solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) )