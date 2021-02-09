# 이진탐색_1_이태경.py
n = int(input())
k = int(input())
lower = 0
upper = k
answer = 0
# i행의 숫자들은 i*1, i*2, i*3, ... i*n으로 구성됨.
# i행의 숫자들 중 m보다 작거나 가은 숫자는 m//i 와 같은 값이 된다.
# Ex) 2행의 숫자들 중 10보다 작거나 같은 숫자는 10//2 => 5개가 된다.

while(lower <= upper):
    mid = (lower + upper) // 2
    count = 0
    #print(lower,mid,upper)

    for i in range(1, n+1):
        # Ex) 2행의 숫자들 중 10보다 작거나 같은 숫자는 10//2 => 5개가 된다.
        # mid//i 값이 n을 넘을 수 있는데 그것을 방지하려고 min함수를 씀.
        count = count + min(mid//i, n)

    if count < k:
        lower = mid + 1
    else: # count >= k
        answer = mid
        upper = mid - 1

print(answer)