# 정수 변환, 딕셔너리, 재귀, while문의 활용, 정수 처리
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    l1 = list(zip(seller, amount))
    result_dic  = defaultdict(int)
    for e in enroll:
        result_dic[e] = 0

    tree_dic = {}
    for e,r in zip(enroll,referral):
        tree_dic[e]=r
    
    for (key,value) in l1:
        money = value * 100
        rate = money // 10
        result_dic[key] = result_dic[key] + money - rate
        x = tree_dic[key]

        while x != '-':
            if rate == 0: break
            tkdskq = rate // 10
            result_dic[x] = result_dic[x] + rate - tkdskq
            rate = rate // 10
            x = tree_dic[x]

    val_list = list(result_dic.values())
    return val_list


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))