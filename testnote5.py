import re,itertools
def solution(user_id, banned_id):
    answer = 0
    gnqh = []
    for bb in banned_id:
        reg = ''
        semi = []
        for b in bb:
            if b == '*':
                reg = reg + '.'
            else:
                reg = reg + b
        

        p = re.compile(reg)
        for uu in user_id:
            m = p.match(uu)
            if m:
                if m.end() == len(uu):
                    semi.append(uu)

        gnqh.append(semi)

    set1 = set()
    for i in range(len(gnqh)):
        l = []
        for j in gnqh[i]:
            l.append(j)
        


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"] ))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))