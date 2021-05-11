import math
def solution(n,a,b):
    r = 1
    while(1):
        d = abs ( a-b )
        if d == 1 and math.ceil ( a / 2 ) == math.ceil ( b / 2 ):
            break

        a = math.ceil ( a / 2 )
        b = math.ceil ( b / 2 )
        r = r + 1

    return r

print(solution(8,2,3))