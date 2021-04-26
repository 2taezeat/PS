import itertools, copy
def solution(expression):
    answer = 0
    answer_list = []
    oper_list = [['+',0],['-',0],['*',0]]
    for e in expression:
        if e == '+':
            oper_list[0][1] += 1
        elif e == '-':
            oper_list[1][1] += 1
        elif e == '*':
            oper_list[2][1] += 1
    exist_oper = []
    for a,b in oper_list:
        if b != 0:
            exist_oper.append(a)
    per = list(itertools.permutations(exist_oper,len(exist_oper)))
    p_c = oper_list[0][1]
    m_c = oper_list[1][1]
    d_c = oper_list[2][1]
    ############################################
    expression = list(expression)
    o_semi = []
    a = ''
    for e in range(len(expression)):
        char = expression[e]
        if not (char == '-' or char == '+' or char == '*'):
            a = a + char
        else:
            o_semi.append(int(a))
            o_semi.append(char)
            a = ''
    o_semi.append(int(a))
    ############################################
    for p in per:
        semi = copy.deepcopy(o_semi)
        for o in p:
            if o == '+':
                ghlttn = p_c
            elif o == '-':
                ghlttn = m_c
            elif o == '*':
                ghlttn = d_c

            for _ in range(ghlttn):
                
                if o == '+':
                    i = 0
                    while(1):
                        if semi[i] == '+':
                            left = i
                            right = i
                            while(1):
                                left = left - 1
                                if left == 0:
                                    left = left - 1
                                    break
                                if semi[left] == '+' or semi[left] == '*'  or semi[left] == '-' :
                                    break
                            
                            while(1):
                                right = right + 1
                                if right == len(semi):
                                    break
                                if semi[right] == '+' or semi[right] == '*' or semi[right] == '-':
                                    break
                            

                            r = semi[left+1] + semi[right-1]
                            del semi[left+1:right]
                            i = left
                            semi.insert(left+1,r)

                        i += 1

                        if i >= len(semi):
                            break

                elif o == '-':
                    i = 0
                    while(1):
                        if semi[i] == '-':
                            left = i
                            right = i
                            while(1):
                                left = left - 1
                                if left == 0:
                                    left = left - 1
                                    break
                                if semi[left] == '+' or semi[left] == '*'  or semi[left] == '-' :
                                    break
                            
                            while(1):
                                right = right + 1
                                if right == len(semi):
                                    break
                                if semi[right] == '+' or semi[right] == '*' or semi[right] == '-':
                                    break
            
                            r = semi[left+1] - semi[right-1]
                            del semi[left+1:right]
                            i = left
                            semi.insert(left+1,r)

                        i += 1

                        if i >= len(semi):
                            break

                elif o == '*':
                    i = 0
                    while(1):
                        if semi[i] == '*':
                            left = i
                            right = i
                            while(1):
                                left = left - 1
                                if left == 0:
                                    left = left - 1
                                    break
                                if semi[left] == '+' or semi[left] == '*'  or semi[left] == '-' :
                                    break
                            
                            while(1):
                                right = right + 1
                                if right == len(semi):
                                    break
                                if semi[right] == '+' or semi[right] == '*' or semi[right] == '-':
                                    break
                            

                            r = semi[left+1] * semi[right-1]
                            del semi[left+1:right]
                            i = left
                            semi.insert(left+1,r)

                        i += 1

                        if i >= len(semi):
                            break

        answer_list.append(abs(semi[0]))


    answer = max(answer_list)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))