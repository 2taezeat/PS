N, M = map(int,input().split())
board = []
for i in range(N):
    a = list(input())
    board.append(a)
answer1 = [
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
]
answer2 = [
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B']
]
counterlist1 = []
counterlist2 = []
for i in range(0,N-7):

    for j in range(0,M-7):
        cut = []
        for k in range(i,i+8):
            cut.append( board[k][j:8+j] )

        sum1 = 0
        sum2 = 0
        for I in range(8):
            for J in range(8):
                if answer1[I][J] != cut[I][J]:
                    sum1 = sum1 + 1

                if answer2[I][J] != cut[I][J]:
                    sum2 = sum2 + 1

        counterlist1.append(sum1)
        counterlist2.append(sum2)

print(min (min(counterlist1),min(counterlist2)) )