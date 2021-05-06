from collections import deque
def solution(n, t, m, timetable):
    timetable.sort()
    time_list = deque()
    now_time = 540
    for ti in timetable:
        a = int(ti[0:2]) *60 + int(ti[3:5])
        time_list.append(a)
    shuttle_count = 0

    while(shuttle_count < n):
        size = 0
        if n - shuttle_count == 1: # 콘이 타야할 막차일때,
            if m == 1:
                answer = min(now_time,time_list[0]-1)
                break
            
            for _ in range(m - 1):
                if not time_list:
                    break
                time_list.popleft()
                if not time_list:
                    break

            if not time_list :
                answer = now_time
            else:
                answer = time_list[0] - 1

            break


        else: #콘이 타야할 막차가 아닐때,
            while( len(time_list) != 0 and time_list[0] <= now_time ):
                time_list.popleft()
                size += 1
                if size >= m:
                    break
            
            shuttle_count += 1
            now_time += t

    h1 = answer // 60
    m1 = answer % 60 
    return '{:02}:{:02}'.format(h1, m1)


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2,1,2,	["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1,1,1,["23:59"]))
# print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))


# print(solution(2,1,5,["23:58"]))
# print(solution(1,1,5,["23:59"]))
# print(solution(2,1,5,["00:01"]))
# print(solution(2,1,1,["00:01"]))

print(solution( 2,10,3,["09:05","09:09","09:13"] ))