N = int(input())
import random
r = []
answer = -1

def sum_digit(number):
    return sum(map(int, str(number)))

for i in range(N):
    i = int(input())

    for j in range(1, 1000000000):
        j = random.randint(1,1000000000)
        s = i*j
        m = sum_digit(s)
        if m % 2 == 1:
            answer = s
            break

    print(answer)