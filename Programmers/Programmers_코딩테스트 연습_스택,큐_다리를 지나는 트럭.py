from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque()
    for i in range(bridge_length):
        q.append(0)
    truck_weights = deque(truck_weights)
    sum1 = 0
    while q:
        time += 1
        b = q.popleft()
        sum1 = sum1 - b
        if truck_weights:
            if sum1 + truck_weights[0] <= weight:
                a = truck_weights.popleft()
                q.append(a)
                sum1 += a
            else:
                q.append(0)
    
    return time


print(solution(2,10,[7,4,5,6]))

#print(solution(100,100,[10]))
#print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))