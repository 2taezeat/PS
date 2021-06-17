def solution(sticker):
    answer = 0
    # table[i] = i번째 index까지의 배열에서 얻을 수 있는 최댓값
    if len(sticker) == 1:
        return sticker[0]

    table = [ 0 for i in range(len(sticker))]


    table[0] = sticker[0]
    table[1] = sticker[0]
    # 맨 앞 스터커를 떼는 경우
    for i in range(2, len(table)-1 ):
        table[i] = max(table[i-1] , table[i-2] + sticker[i] )
        # 1) 만약 i-1번 스티커를 뗏을 경우, i번재 스티커를 뗄 수 없다
        # 2) 만약 i-1번 스터커를 떼지 않았을 경우 = i-2번까지의 최댓값 + i번째 스티커의 값


    table2 = [ 0 for i in range(len(sticker))]

    table2[1] = sticker[1]
    # 맨 앞 스터커를 떼지 않는 경우
    for i in range(2, len(table) ):
        table2[i] = max(table2[i-1] , table2[i-2] + sticker[i] )

    answer = max(table[-2], table2[-1])
    return answer