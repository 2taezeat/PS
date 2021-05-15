def solution(skill, skill_trees):
    answer = 0
    for ss in skill_trees:
        i = 0
        q = 0
        for s in ss:
            if s in skill:
                if s != skill[i]:
                    q = 1
                    break

                i += 1
        if q == 0:
            answer += 1


    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))