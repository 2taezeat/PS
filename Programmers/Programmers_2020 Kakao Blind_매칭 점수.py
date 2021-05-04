import re
from collections import defaultdict
def solution(word, pages):
    word = word.lower()
    dic = {}
    result_dic = {}
    answer = []
    for p in pages:
        split_p = re.split('"| />|/>|=|\n|>| |<|"\\"', p)
        basic_count = 0
        outer_link = 0
        ###
        t_p =  re.split('[^a-zA-Z]',p)
        for s1 in t_p:
            s1 = s1.lower()
            if s1 == word:
                basic_count += 1
        ###
        m = 0
        h = 0
        for i in range(len(split_p)):
            print(split_p[i])
            if split_p[i] == 'meta':
                m = 1

            if m == 1:
                if re.findall("https://",split_p[i]):
                    key = split_p[i]
                    dic[key] = []
                    result_dic[key] = []
                    m = 0


            if split_p[i] == 'href':
                h = 1

            if h == 1:
                if re.findall("https://",split_p[i]):
                    dic[key].append( split_p[i] )
                    outer_link += 1
                    h = 0

        dic[key].append(basic_count)
        result_dic[key].append(basic_count)
        dic[key].append(outer_link)

    for (key,value) in dic.items():
        leg = len(value)
        for v in range(leg-2):
            try:
                result_dic[ value[v] ].append( dic[key][-2] / dic[key][-1] )
            except:
                pass
    
    i = 0
    for (key,value) in result_dic.items():
        answer.append((i,sum(value)))
        i = i + 1

    answer.sort( key = lambda x : (-x[1], x[0]) )
    print(answer)
    return answer[0][0]


print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
