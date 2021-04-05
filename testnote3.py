dice_list = list ( map(int,input().split()) )
space = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,22,24,28,27,26,25,30,35,0]
akf_scroe = [[0,0], [0,0], [0,0], [0,0]] #(위치, 점수)
answer2 = 0
def next_locate(a, M):
    if (0<= a <= 4) or (6<= a <= 9) or (11<= a <= 14): nl = a + M    
    elif a == 5:
        nl = 20 + M
        if nl >= 24:
            nl = 29 + (M-4)
    elif a == 10:
        nl = 23 + M
        if nl >= 26:
            nl = 29 + (M-3)
    elif a == 15: nl = 25 + M
    elif a == 20 or a == 32: nl = 32

    elif a == 16:
        if M == 1: nl = 17
        elif M == 2: nl = 18
        elif M == 3: nl = 19
        elif M == 4: nl = 20
        elif M == 5: nl = 32
    elif a == 17:
        if M == 1:  nl = 18
        elif M == 2:  nl = 19
        elif M == 3:  nl = 20
        elif M == 4:  nl = 32
        elif M == 5:  nl = 32
    elif a == 18:
        if M == 1:  nl = 19
        elif M == 2:  nl = 20
        elif M == 3:  nl = 32
        elif M == 4:  nl = 32
        elif M == 5:  nl = 32
    elif a == 19:
        if M == 1:  nl = 20
        elif M == 2:  nl = 32
        elif M == 3:  nl = 32
        elif M == 4:  nl = 32
        elif M == 5:  nl = 32

    elif a == 29:
        if M == 1: nl = 30
        elif M == 2: nl = 31
        elif M == 3: nl = 20
        elif M == 4: nl = 32
        elif M == 5: nl = 32
    elif a == 30:
        if M == 1:  nl = 31
        elif M == 2:  nl = 20
        elif M == 3:  nl = 32
        elif M == 4:  nl = 32
        elif M == 5:  nl = 32
    elif a == 31:
        if M == 1:  nl = 20
        elif M == 2:  nl = 32
        elif M == 3:  nl = 32
        elif M == 4:  nl = 32
        elif M == 5:  nl = 32

    elif a == 21:
        if M == 1: nl = 22
        elif M == 2: nl = 23
        elif M == 3: nl = 29
        elif M == 4: nl = 30
        elif M == 5: nl = 31
    elif a == 22:
        if M == 1: nl = 23
        elif M == 2: nl = 29
        elif M == 3: nl = 30
        elif M == 4: nl = 31
        elif M == 5: nl = 20
    elif a == 23:
        if M == 1: nl = 29
        elif M == 2: nl = 30
        elif M == 3: nl = 31
        elif M == 4: nl = 20
        elif M == 5: nl = 32

    elif a == 24:
        if M == 1: nl = 25
        elif M == 2: nl = 29
        elif M == 3: nl = 30
        elif M == 4: nl = 31
        elif M == 5: nl = 20
    elif a == 25:
        if M == 1: nl = 29
        elif M == 2: nl = 30
        elif M == 3: nl = 31
        elif M == 4: nl = 20
        elif M == 5: nl = 32

    elif a == 26:
        if M == 1: nl = 27
        elif M == 2: nl = 28
        elif M == 3: nl = 29
        elif M == 4: nl = 30
        elif M == 5: nl = 31
    elif a == 27:
        if M == 1: nl = 28
        elif M == 2: nl = 29
        elif M == 3: nl = 30
        elif M == 4: nl = 31
        elif M == 5: nl = 20
    elif a == 28:
        if M == 1: nl = 29
        elif M == 2: nl = 30
        elif M == 3: nl = 31
        elif M == 4: nl = 20
        elif M == 5: nl = 32

    ## 범위 초과 체크
    if nl >= 32:
        nl = 32
    
    return nl
        
def whichakf(I,M):
    global space
    global akf_scroe
    q = 0

    for k in range(4):
        nl = next_locate( akf_scroe[I][0], M)
        if nl == 32:
            continue

        if nl == akf_scroe[k][0]:
            q = 1
            break
    if q == 0:
        return [akf_scroe[I][0], nl] #(움직이기 전 위치, 움직인 위치)

def dfs(dice_count):
    global space
    global akf_scroe
    global answer
    global answer2
    if dice_count > 9:
        return
    move = dice_list[dice_count] # move : 1 ~ 5
    # 4개의 말중 어느 말을 움직일지 정하기
    l1 = [] #(움직이기 전 위치, 움직인 위치, 몇번말)     의 리스트
    for i in range(0,4):
        c = whichakf(i, move)
        if c:
            l1.append( c + [i] )

    # 움직이기
    for l in range(len(l1)):
        before_w = l1[l][0]
        mving_w = l1[l][1]
        num_akf = l1[l][2]
        if before_w == mving_w:
            continue

        # moving
        get_score = space[mving_w]
        akf_scroe[num_akf][1] = get_score + akf_scroe[num_akf][1]
        akf_scroe[num_akf][0] = mving_w
        
        # 각 l1의 case마다의 점수합을 result에 추가하기
        answer2 = answer2 + get_score
        answer.append(answer2)

        dfs(dice_count+1)

        #de_moving
        answer2 = answer2 - get_score
        akf_scroe[num_akf][0] = before_w
        akf_scroe[num_akf][1] = akf_scroe[num_akf][1] - get_score

dfs(0)
print(max(answer))