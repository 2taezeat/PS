import re
def solution(files):
    result = []
    j = 0
    for f in files:
        h = 0
        n = 0
        idx_n = 0
        num_count = 0
    
        for i in range(len(f)):
            if (h == 0) and (f[i] == '0' or f[i] == '1' or f[i] == '2' or f[i] == '3' or f[i] == '4' or f[i] == '5' or f[i] == '6' or f[i] == '7' or f[i] == '8' or f[i] == '9'):
                h = 1
                idx_h = i
            
            if h == 1:
                if (n == 0) and f[i] == '0' or f[i] == '1' or f[i] == '2' or f[i] == '3' or f[i] == '4' or f[i] == '5' or f[i] == '6' or f[i] == '7' or f[i] == '8' or f[i] == '9':
                    num_count += 1
                elif n == 0:
                    n = 1
                    idx_n = i
                    

            if h == 1 and n == 0 and num_count > 5:
                idx_n = i
                n = 1

        if idx_n == 0:
            head = f[:idx_h]
            number = f[idx_h:]
        else:
            head = f[:idx_h]
            number = f[idx_h:idx_n]

        tail = f[idx_n:]
        head = head.lower()
        number = int(number)
        result.append((head,number,j,tail,f))
        j = j + 1

    result.sort(key = lambda x: (x[0],x[1],x[2]) )
    answer = []
    for a in result:
        answer.append(a[-1])
    
    return answer

print(solution(["F-15"]))
#print(solution(["foo010bar020.zip"]))
#print(solution(["foo010020bar.zip"]))
#print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
#print('------------------')
#print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))