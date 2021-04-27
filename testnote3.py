import re,itertools
def solution(user_id, banned_id):
    answer = 0
    gnqh = []
    per = list( itertools.permutations(user_id, len(banned_id)))
    b_reg = []

    for bb in banned_id:
        reg = ''
        for b in bb:
            if b == '*':
                reg = reg + '.'
            else:
                reg = reg + b
        b_reg.append(reg)



        p = re.compile(reg)
        for uuu in per:
            #print(uu)
            for uu in uuu:

                m = p.match(uu)
                if m:
                    if m.end() == len(uu):
                        semi.append(uu)

        gnqh.append(set(semi))

    #print(gnqh,len(gnqh))
    print(gnqh)
    if gnqh == []:
        return 0

    a = list(itertools.product(*gnqh))

            
    

    set1 = set()
    for aa in a:
        sa = set(aa)
        set1.add( tuple(sa) )

    #print(set1)

    for s in set1:
        if len(s) == len(gnqh):
            answer += 1
    return answer



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"] ))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))