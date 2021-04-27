def solution(new_id):
    new_id = new_id.lower()
    new_id_list = list(new_id)
    new_id_2 = []
    for i in new_id_list:
        if i == '-' or i == '.' or i == '_' or 48 <= ord(i) <=57 or 97 <= ord(i) <=122:
            new_id_2.append(i)
    # 3.
    j = 0
    while(1):
        if j >= len(new_id_2)-1:
            break
        if new_id_2[j] == '.' and new_id_2[j+1] == '.':
            new_id_2.pop(j)
            j = j - 1

        j = j + 1

    # 4.
    if new_id_2[0] == '.':
        new_id_2.pop(0)
    if new_id_2 and new_id_2[-1] == '.':
        new_id_2.pop()
    # 5.
    if new_id_2 == []:
        new_id_2.append('a')
    # 6.
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2[0:15]
    if new_id_2[-1] == '.':
        new_id_2.pop()
    # 7.
    if len(new_id_2) <= 2:
        while(1):
            last = new_id_2[-1]
            new_id_2.append(last)
            if len(new_id_2) >= 3:
                break

    answer = ''.join(new_id_2)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))