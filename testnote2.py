import copy
N, L = map(int,input().split())
o_space = []
o2_space = []
for i in range(N):
    list1 = list(map(int,input().split()))
    l2 = []
    l3 = []
    for l in list1:
        l2.append([l,100])

    # for l in list1[::-1]:
    #     l3.append([l,False])
    o_space.append(l2)

    o2_space.append(l3)
answer1 = []
answer2 = []

# 가로 확인
for i in range(N):
    judge = True
    for k in range(N-L):
        l1 = o_space[i][k:k+L+1]
        maxl1 = max(l1)
        minl1 = min(l1)
        diff = maxl1[0] - minl1[0]

        if diff == 1:
            for l in range(len(l1)):

                if l1[l][0] == (maxl1[0] - 1) and l1[l][1] == 100:
                    for lth in range(L):
                        if (k+lth+l < N) and ( o_space[i][k+l+lth][0] == l1[l][0] ):
                            o_space[i][k+l+lth][1] = 200

                        else:
                            judge = False
                            break

                elif l1[l][0] == (minl1[0]) and l1[l][1] == 100:
                    for lth in range(L):
                        if (k+lth+l < N) and ( o_space[i][k+l+lth][0] == l1[l][0] ):
                            o_space[i][k+l+lth][1] = 300

                        else:
                            judge = False
                            break

        elif diff != 0 :
            judge = False
            break
            
    for m in range(0,N-1):
        # if o_space[i][m][1] == 200 and o_space[i][m+1][0] - o_space[i][m][0] == 1:
        #     judge = False
        #     break
        if o_space[i][m][1] == 300 and o_space[i][m+1][0] - o_space[i][m][0] == 1:
            print(123123)
            judge = False
            break



    print(o_space[i])
    print(judge)
    print('--------------------')

    if judge:
        answer1.append(i)

print(answer1)