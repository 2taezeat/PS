from itertools import combinations

def primecheck(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for (a,b,c) in combinations(nums,3):
        sum1 = a+b+c
        if primecheck(sum1):
            answer+=1
    return answer 


print(solution([[1,2,7,6,4]]))
