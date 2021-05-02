from collections import defaultdict

def recrusion(name,rottn):
    global seller_dic
    global result_dic
    global tree_dic
    if name == 'center':
        return

    #price = rottn * 100
    result_dic[name] = result_dic[name] + rottn
    tkdska = int( rottn * 0.1 )
    result_dic[name] = result_dic[name] - tkdska
    
    nxt_name = tree_dic[name][0]
    #nxt_rottn = skajwal
    #print(result_dic)
    #print(nxt_name,tkdska)

    recrusion(nxt_name, tkdska)


def solution(enroll, referral, seller, amount):
    l1 = list(zip(seller, amount))
    global seller_dic
    global result_dic
    global tree_dic

    seller_dic  = defaultdict(int)
    for (a,b) in l1:
        seller_dic[a] = seller_dic[a] + b
    result_dic  = defaultdict(int)
    for e in enroll:
        result_dic[e] = 0
    tree_dic = {}
    for i in range(len(enroll)):
        A = enroll[i]
        B = referral[i]
        if B =='-':
            B = 'center'
        
        tree_dic[A] = tree_dic.get(A, []) + [B]
        #dic[B] = dic.get(B, []) + [A]

    # print(seller_dic)
    # print(result_dic)
    # print(tree_dic)
    # print('-------------------')


    #recrusion("young",12*100)
    

    for (key,value) in seller_dic.items():
        recrusion(key,value*100)

    #print(result_dic)

    val_list = list(result_dic.values())
    #print(val_list)
    #answer = []
    return val_list




print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4]))
