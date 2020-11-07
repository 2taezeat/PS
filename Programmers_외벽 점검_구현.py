# 구현_4_이태경.py
from itertools import permutations, combinations, product
import copy
# 모두 외벽점검했는지 체크하는 함수
def check(list1,w_c):
    count = 0
    for l in list1:
        if l == 1:
            count = count + 1
            
    if count//2 >= w_c:
        return True
    else:
        return False

def solution(n, weak, dist):
    per = []
    answer_list = []
    standard = len(weak)
    # 원형 배열을 2배늘려 1차원 리스트로 만듬.
    weaklist = [0] *(n*2)
    for i in range(len(weak)):
        weak.append(weak[i]+n)

    for i in weak:
        weaklist[i] = 1

    for i in range(1, len(dist)+1):
        a = list(permutations(dist,i))
        for j in a:
            per.append(j)


    for p in per:

        for d in p:
            #c_weaklist = copy.deepcopy(weaklist)
            for i in weak:
                c_weaklist = copy.deepcopy(weaklist)
                I = (d+i) % 24
                #print(I)
                count = 0
                for j in range(i, I+1):
                    if j > (n*2)-1:
                        j = j % (24)

                    print(j)
                    if c_weaklist[j] == 1:
                        count = count + 1 
                    #c_weaklist[j] = c_weaklist[j] * 0

            
                print(count)

                if count == standard:
                    return True
            #print('-------------------------------')
                #val = check(c_weaklist,len(weak)//2)
                #answer_list.append([val,len(p)])
        

    #print(answer_list)
    for i in range(len(answer_list)):
        if answer_list[i][0] == True:
            return answer_list[i][1]

    return False



print(solution (12, [1, 5, 6, 10], [1, 2, 3, 4])  )