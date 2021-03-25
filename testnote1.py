import copy
N, L = map(int,input().split())
o_space = []
for i in range(N):
    list1 = list(map(int,input().split()))
    l2 = []
    for l in list1:
        l2.append([l,100])
    o_space.append(l2)

answer1 = []
answer2 = []

# 가로 확인
for i in range(N):
    judge = True
    for k in range(N-L):
        part = o_space[i][k:k+L+1]
        print(l1)

        for p in range(0, len(part)-1):
            if part[p+1][0] - part[p][0] = 1:
                

            elif part[p+1][0] - part[p][0] = -1:






        if diff == 1:
            pass
        elif diff != 0 :
            judge = False
            break

            



    # print(o_space[i])
    # print('--------------------')

    # if judge:
    #     answer1.append(i)

print(answer1)