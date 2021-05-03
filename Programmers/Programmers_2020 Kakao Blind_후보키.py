import itertools
def fun1(checked,cc):
    for ch in checked:
        q = 0
        for b in ch:
            if b in cc: q = q + 1
            if q == len(ch): return False
            
    return True

def solution(relation):
    answer,count = 0, 1
    kate = len(relation[0])
    kate_list = [i for i in range(kate)]
    checked = []
    while( count < kate+1 ):
        ccc = list(itertools.combinations(kate_list,count))
        for cc in ccc:
            tmp = []
            if fun1(checked,cc) == False:
                continue

            for c in cc:
                semi = []
                for r in relation: semi.append(r[c])
                tmp.append(semi)

            final = list(zip(*tmp))

            if len(final) == len(set(final)):
                checked.append(cc)
                answer += 1

        count = count + 1

    return answer
        

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]) )