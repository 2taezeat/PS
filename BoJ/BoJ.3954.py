def matching(pro):
    m_l = []
    stack = []
    for p in range(len(pro)):
        if pro[p] =='[':
            stack.append(p)

        elif pro[p] == ']':
            a = stack.pop()
            m_l.append((a,p))
    return m_l
    
testcase = int(input())
for t in range(testcase):
    m,c,i = map(int,input().split())
    program = list(input())
    input_pro = list(map(ord, input())) + [255]
    pointer = 0
    ip_idx = 0
    array = [0 for _ in range(m)]
    pro_idx = 0 # 프로그램 내의 인덱스
    count = 0 # 프로그램 '수행' 횟수
    match_list = matching(program)
    q = 0
    one_more = 0

    while(pro_idx < c):
        p = program[pro_idx]
        if count >= 50000000:
            q = 1
            one_more = 1
            break

        if p == '>':
            pointer = (pointer + 1) % m
            pro_idx += 1

        elif p == '<':
            pointer = (pointer - 1) % m
            pro_idx += 1

        elif p == '-':
            array[pointer] = (array[pointer] - 1) % pow(2,8)
            pro_idx += 1

        elif p == '+':
            array[pointer] = (array[pointer] + 1) % pow(2,8)
            pro_idx += 1

        elif p == '[':
            if array[pointer] == 0:
                for m0,m1 in match_list:
                    if m0 == pro_idx:
                        pro_idx = m1 + 1
                        break
            else:
                pro_idx += 1

        elif p == ']':
            if array[pointer] != 0: # 다시 '[' + 1로 감.
                for m0,m1 in match_list:
                    if m1 == pro_idx:
                        pro_idx = m0 + 1
                        break

            else: # 루프 빠져 나오기
                pro_idx += 1

        elif p == '.':
            pro_idx += 1

        elif p == ',':
            array[pointer] = input_pro[ip_idx]
            if ip_idx < i:
                ip_idx +=1
            pro_idx += 1

        count += 1

    if q == 0:
        print('Terminates')

    elif q == 1:
        qjadnl = []
        while(pro_idx < c):
            p = program[pro_idx]

            if p == '>':
                pointer = (pointer + 1) % m
                pro_idx += 1

            elif p == '<':
                pointer = (pointer - 1) % m
                pro_idx += 1

            elif p == '-':
                array[pointer] = (array[pointer] - 1) % pow(2,8)
                pro_idx += 1

            elif p == '+':
                array[pointer] = (array[pointer] + 1) % pow(2,8)
                pro_idx += 1

            elif p == '[':
                if array[pointer] == 0:
                    for m0,m1 in match_list:
                        if m0 == pro_idx:
                            pro_idx = m1 + 1
                            break
                else:
                    pro_idx += 1

            elif p == ']':
                if array[pointer] != 0: # 다시 '[' + 1로 감.
                    for m0,m1 in match_list:
                        if m1 == pro_idx:
                            pro_idx = m0 + 1
                            break

                else: # 루프 빠져 나오기
                    pro_idx += 1

            elif p == '.':
                pro_idx += 1

            elif p == ',':
                array[pointer] = input_pro[ip_idx]
                if ip_idx < i:
                    ip_idx +=1
                pro_idx += 1

            count += 1
            # 움직인 범위 계산
            if pro_idx not in qjadnl:
                qjadnl.append(pro_idx)
    
            if count >= 50000000 + 50000000:
                right = max(qjadnl)
                for m0,m1 in match_list:
                    if m1 == right:
                        left = m0
                        break
            
                print('Loops',left,right)
                break