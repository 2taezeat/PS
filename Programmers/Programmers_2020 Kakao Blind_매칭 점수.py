import re
from collections import defaultdict
def solution(word, pages):
    # dic = defaultdict(list)
    # cont = re.compile("content")
    # c = cont.search(pages[0])
    # b = c.start()
    # for i in range(b,len(pages[0])):
    # #print(pages[0][126:133])
    # l1 = pages[0].split(' ')

    # # for i in range(len(l1)):
    # #     print(i,l1[i])

    word = word.lower()
    dic = defaultdict(list)
    info = []

    b = re.split("=|\n|/>| ",pages[0])
    print(b)

    for p in pages:
        split_p = re.split("=|\n|/>| ",p)
        text = ''
        b = 0
        basic_count = 0
        tmp = []
        for i in range(len(split_p)):
            if split_p[i] == 'content':
                #dic[split_p[i+1]] = []
                tmp.append(split_p[i+1])

            if split_p[i] == '<body>':
                b = 1

            if b == 1:
                #text.append(split_p[i])
                text = text + split_p[i] + ' '
                if split_p[i] == '<a':
                    b = 0

        split_text = re.split('[^a-z^A-Z]',text)

        for s1 in split_text:
            s1 = s1.lower()
            if s1 == word:
                basic_count += 1

        tmp.append(basic_count)

        info.append(tmp)


    print(info)


    print('--------------')



print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))