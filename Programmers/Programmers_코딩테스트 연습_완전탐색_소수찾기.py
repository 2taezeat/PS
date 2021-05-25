from itertools import permutations
def primecheck(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    list1 = set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            list1.add(int(''.join(p)))
    answer = 0

    for t in list1:
        if primecheck(t):
            answer += 1
        
    return answer

print(solution("17"))
print(solution("011"))