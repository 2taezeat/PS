from collections import defaultdict
def solution(record):
    answer = []
    el_list = []
    user_id_dic = defaultdict(str)
    for r in record:
        rl = r.split(' ')
        if rl[0] == 'Enter':
            user_id = rl[1]
            el_list.append(('E',user_id))
            user_id_dic[user_id] = rl[2]

        elif rl[0] == 'Leave':
            user_id = rl[1]
            el_list.append(('L',user_id))

        elif rl[0] == 'Change':
            user_id = rl[1]
            user_id_dic[user_id] = rl[2]

    for (state,uid) in el_list:
        if state == 'E':
            name = user_id_dic[uid]
            answer.append(name+"님이 들어왔습니다.")
        elif state == 'L':
            name = user_id_dic[uid]
            answer.append(name+"님이 나갔습니다.")

    return answer



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))