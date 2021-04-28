import re
def solution(info, query):
    list1 = []
    result = []
    for i in range(len(info)):        
        aa = info[i].split(' ')
        d = dict()
        d['lag'] = aa[0]
        d['job'] = aa[1]
        d['car'] = aa[2]
        d['food'] = aa[3]
        d['score'] = int(aa[4])
        list1.append(d)
            
    #print(list1)
    #print()
    query1 = []
    for i in range(len(query)):
        bb = re.split(' |and',query[i])
        #query1.append(bb)
        person_count = 0

        l = bb[0]
        j = bb[3]
        c = bb[6]
        f = bb[9]
        s = int(bb[10])

        for lst in list1:
            # print(lst['lag'],l)
            # print(lst['job'],j)
            # print(lst['car'],c)
            # print(lst['food'],f)
            # print(lst['score'],s)

            # if (l == '-' or lst['lag'] == l) and (j == '-' or lst['job'] == j) and (c == '-' or lst['car'] == c) and (f == '-' or lst['food'] == f) and lst['score'] >= s:
            #     print(lst)
            #     person_count += 1

            if (l == '-' or lst['lag'] == l):
                if (j == '-' or lst['job'] == j):
                    if (c == '-' or lst['car'] == c):
                        if (f == '-' or lst['food'] == f):
                            if lst['score'] >= s:
                                person_count += 1

        #    print('----------------')

        #print(person_count)
        result.append(person_count)

        

    return result






print(solution( ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]))