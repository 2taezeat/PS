import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    r = []
    j = 0
    i = 0
    T = t*m
    while True:
        if j > T:
            break
        a = convert(i,n)
        r.append( convert(i,n).upper() )
        j = j + len(a)
        i = i + 1

    r = "".join(r)

    for i in range(p-1,T,m):
        answer = answer + r[i]
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
#print(solution(,,,))

