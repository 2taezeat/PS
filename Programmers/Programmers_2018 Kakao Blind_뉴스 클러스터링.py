from collections import Counter, defaultdict
def solution(str1, str2):
    set1 = []
    set2 = []
    l1 = list(str1)
    l2 = list(str2)

    for i in range(0, len(l1) -1 ):
        c1 = l1[i].lower()
        c2 = l1[i+1].lower()
        o1 = ord(c1)
        o2 = ord(c2)
        if 97<= o1 <=122 and 97<= o2 <=122: set1.append(c1+c2)

    for i in range(0, len(l2) -1 ):
        c1 = l2[i].lower()
        c2 = l2[i+1].lower()
        o1 = ord(c1)
        o2 = ord(c2)
        if 97<= o1 <=122 and 97<= o2 <=122: set2.append(c1+c2)

    counter1 = Counter(set1)
    counter2 = Counter(set2)

    if set1 == [] and set2 == []:
        return 1 * 65536

    set1 = set(set1)
    set2 = set(set2)

    inter =  set1 & set2
    union = set1 | set2

    in_count = 0
    un_count = 0

    for u in list(union):
        un_count += max(counter1[u], counter2[u])

    for i in list(inter):
        in_count += min(counter1[i], counter2[i])

    answer = in_count / un_count 
    return int ( answer * 65536 )




print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))