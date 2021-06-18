move = []
def hanoi(n,a,b,c):
    if n == 1:
        move.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)

def solution(n):
    hanoi(n,1,2,3)
    return move


print(solution(2))