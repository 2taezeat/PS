from itertools import product
# import copy
def solution(numbers, target):
    # 시간초과
    # answer = 0 
    # pro = list ( product(['+','-'], repeat=len(numbers)))
    # tmp = []
    # for i in range(len(numbers)*2):
    #     if i % 2 == 0:
    #         tmp.append('#')
    #     else:
    #         tmp.append(str(numbers[(i-1)//2]))

    # for p in pro:
    #     c_numbers = copy.deepcopy(tmp)
    #     for i in range(len(p)):
    #         c_numbers[i*2] = p[i]

    #     if eval(''.join(c_numbers)) == target:
    #         answer += 1
    # return answer
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)



print(solution([1,1,1,1,1],3))