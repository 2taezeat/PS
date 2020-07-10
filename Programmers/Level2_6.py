from math import gcd

def solution(arr):

    i = 0

    while( len(arr) != 1):
        lcm1 = (arr[i] * arr[i+1]) // gcd(arr[i], arr[i+1])

        arr.pop(0)
        arr.pop(0)
        arr.insert(0,lcm1)

    return (arr[0])
    




print(solution([2,6,8,14]))