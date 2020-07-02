def solution(people, limit):
    people.sort()
    answer = 0
    start_cursor = 0
    end_cursor = len(people) - 1
    
    while (start_cursor <= end_cursor):

        if people[end_cursor] + people[start_cursor] > limit:
            end_cursor -= 1

        else:
            start_cursor += 1
            end_cursor -= 1

        answer = answer + 1

    return answer

