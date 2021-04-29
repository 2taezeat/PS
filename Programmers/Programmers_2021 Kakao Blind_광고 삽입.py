def solution(play_time, adv_time, logs):
    log = []
    result = []
    adv_time = list(adv_time)
    play_time = list(play_time)
    play_s = 0
    play_s = play_s + (int(play_time[0])*3600)*10
    play_s = play_s + (int(play_time[1])*3600)
    play_s = play_s + int(play_time[3])*60*10
    play_s = play_s + int(play_time[4])*60
    play_s = play_s + int(play_time[6])*10
    play_s = play_s + int(play_time[7])*1

    adv_s = 0
    adv_s = adv_s + (int(adv_time[0])*3600)*10
    adv_s = adv_s + (int(adv_time[1])*3600)
    adv_s = adv_s + int(adv_time[3])*60*10
    adv_s = adv_s + int(adv_time[4])*60
    adv_s = adv_s + int(adv_time[6])*10
    adv_s = adv_s + int(adv_time[7])*1
    time_list = [0 for _ in range(play_s+1)]

    for i in logs:
        i = list(i)
        start_s = 0
        end_s = 0
        start_s = start_s + (int(i[0])*3600)*10
        start_s = start_s + (int(i[1])*3600)
        start_s = start_s + int(i[3])*60*10
        start_s = start_s + int(i[4])*60
        start_s = start_s + int(i[6])*10
        start_s = start_s + int(i[7])*1

        end_s = end_s + (int(i[9])*3600)*10
        end_s = end_s + (int(i[10])*3600)
        end_s = end_s + int(i[12])*60*10
        end_s = end_s + int(i[13])*60
        end_s = end_s + int(i[15])*10
        end_s = end_s + int(i[16])*1
        log.append((start_s,end_s))
        time_list[start_s] = time_list[start_s] + 1
        time_list[end_s] = time_list[end_s] - 1

    for i in range( 1, len(time_list) ):
        time_list[i] = time_list[i] + time_list[i-1]

    for i in range( 1, len(time_list) ):
        time_list[i] = time_list[i] + time_list[i-1]

    for i in range(0,len(time_list)-adv_s):
        j = i + adv_s
        a = time_list[j] - time_list[i]
        result.append((i,j,a))

    result = sorted(result, key = lambda x : (-x[2], x[0]))

    if result[0][0] == 0:
        return '00:00:00'

    res = result[0][0] + 1
    hour = res // 3600
    minute = ( res - (hour*3600) ) // 60 
    sec = (res - (hour*3600) - (minute*60) )

    if 0<= hour <= 9:
        hour_str = '0' + str(hour)
    else:
        hour_str = str(hour)

    if 0<= minute <= 9:
        minute_str = '0' + str(minute)
    else:
        minute_str = str(minute)

    if 0<= sec <= 9:
        sec_str = '0' + str(sec)
    else:
        sec_str = str(sec)

    answer = hour_str+':'+minute_str+':'+sec_str
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))