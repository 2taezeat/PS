import sys
T = int(sys.stdin.readline())

for i in range(T):
    A = []
    N = int(sys.stdin.readline())

    for j in range(N):

        a,b = map(int,sys.stdin.readline().split())

        A.append((a,b))

    count = 0
    A.sort()

    stand = A[0][1]
    for k in range(N - 1):
        if stand < A[k + 1][1]:
            count = count + 1
        else:
            stand = A[k + 1][1]

    answer = N - count
    print(answer)