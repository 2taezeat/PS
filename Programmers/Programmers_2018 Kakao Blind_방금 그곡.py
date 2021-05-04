import re
def solution(m, musicinfos):
    result = {}
    j = 0
    m = re.sub('C#', 'Z', m)
    m = re.sub('D#', 'Y', m)
    m = re.sub('F#', 'X', m)
    m = re.sub('G#', 'W', m)
    m = re.sub('A#', 'U', m)

    for mm in musicinfos:
        sm = mm.split(',')
        s = sm[0]
        e = sm[1]
        title = sm[2]
        dma = sm[3]
        dma = re.sub('C#', 'Z', dma)
        dma = re.sub('D#', 'Y', dma)
        dma = re.sub('F#', 'X', dma)
        dma = re.sub('G#', 'W', dma)
        dma = re.sub('A#', 'U', dma)

        result[title] = []
        hour = int(e[0:2]) - int(s[0:2])
        minute = int(e[3:5]) - int(s[3:5])
        time_diff = hour*60 + minute
        length = len(dma)

        music = 0
        if length > time_diff:
            music = dma[:time_diff]
        else:
            music = dma * (time_diff // length) 
            music = music + dma[:time_diff % length]        

        result[title].append( (time_diff,j,music) )
        j += 1

    answer = []

    for (k,v) in result.items():
        b = re.findall(m,v[0][2])
        if b :
            answer.append((k, v[0][0], v[0][1]))

    if answer == []:
        return '(None)'

    answer.sort(key = lambda x: (-x[1],x[2]) )
    return answer[0][0]



print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
