from collections import defaultdict
def solution(enroll, referral, seller, amount):
    l1 = list(zip(seller, amount))
    seller_dic  = defaultdict(int)
    for (a,b) in l1:
        seller_dic[a] = seller_dic[a] + b
    result_dic  = defaultdict(int)
    for e in enroll:
        result_dic[e] = 0
    print(seller_dic)
    print(result_dic)








    answer = []
    return answer




print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4]))
