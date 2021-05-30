from math import factorial
def solution(n, k):
    answer = []
    a = [ i for i in range(1,n+1)]
    
    while n != 0:
        
        f = factorial(n)
        v = f // n
        s = a.pop(((k-1) // v))
        
        answer.append( s )
        n = n - 1
        k = k % v

    return answer


print(solution(3,5))