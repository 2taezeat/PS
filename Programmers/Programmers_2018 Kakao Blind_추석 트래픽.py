def solution(lines):
    result = []
    for l in lines:
        l0 = l[11:23]
        hour = int(l0[0:2]) * 3600
        minute = int(l0[3:5]) * 60
        sec = int(l0[6:8])
        s = hour + minute + sec
        ms = (s*1000) + int(l0[9:12])
        v = int(l[24]) * 1000
        if l[26:-1] != '':
            v = v + int(l[26:-1])

        end = ms
        start = end - v + 1
        result.append((start, end))

    a = [1]
    for (s1,e1) in result:
        ans = 0
        start1 = s1
        end1 = s1 + 1000
        for (ss,ee) in result:
            if ee >= start1 and ss < end1:
                ans += 1
    
        a.append(ans)

    for (s2,e2) in result:
        ans = 0
        start2 = e2
        end2 = e2 + 1000
        for (ss,ee) in result:
            if ee >= start2 and ss < end2:
                ans += 1

        a.append(ans)

    return max(a)

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
# print(solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]))