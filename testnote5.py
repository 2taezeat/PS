import re
def solution(s):
    split_s = re.split('{|}|,',s)
    arr = []
    p = []
    for i in range(len(split_s)):
        if split_s[i] == '' or split_s[i] == ' ':
            if p != []:
                arr.append(p)
                p = []
        else:
            p.append(split_s[i])
        
    semi = []
    for a in arr:
        semi.append( (len(a),a) )


    semi.sort()
    answer = []
    for se in semi:
        for k in se[1]:
            if k not in answer and k != ',':
                answer.append(k)

    answer = list(map(int,answer))
    return answer



        



print( solution ( "{ {1,2,3},{2,1},{1,2,4,3},{2} }" ) )
print( solution ( "{{20,111},{111}}" ) )
#print( solution ( "{{123}}" ) )