from collections import defaultdict
def solution(gems):
    set_gem = set(gems)
    length = len(set_gem)
    dict1 = defaultdict(int)
    a1, a2 = 0, 999999999
    for i in range(len(gems)):

        if dict1[gems[i]] != 0:
            del dict1[gems[i]]
            dict1[gems[i]] = i + 1
        else:
            dict1[gems[i]] = i + 1

        if len(dict1) == length:
            vl = list(dict1.values())
            if vl[-1] == vl[0]:
                return vl[0], vl[-1]
            else:
                if a2-a1 > vl[-1]-vl[0]:
                    a1 = vl[0]
                    a2 = vl[-1]

    return a1,a2
    
#print( solution(["DIA", "RUBY", "RUBY", "RUBY", "RUBY", "EMERALD", "SAPPHIRE", "DIA"]) )
#print( solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) )
# print( solution(["AA", "AB", "AC", "AA", "AC"]) )
# print( solution(["XYZ", "XYZ", "XYZ"]) )
# print( solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) )