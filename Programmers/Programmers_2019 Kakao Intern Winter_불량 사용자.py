import re,itertools
def solution(user_id, banned_id):
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
    
    if b_reg == []:
        return 0

    for uuu in per:
        tmp = set()

        for uu in range(len(uuu)):
            q = 0
            b = b_reg[uu]
            p = re.compile(b)
            m = p.match(uuu[uu])

            if m and (m.end() == len(uuu[uu])):
                tmp.add(uuu[uu])
            else:
                q = 1

        
        if len(tmp) == len(banned_id) and q == 0:
            if tmp not in gnqh:
                gnqh.append(tmp)
        
    return len(gnqh)



# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"] ))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))