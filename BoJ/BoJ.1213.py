st = input()
s = list(st)
e,o = 0,0
s.sort()
alp = [0]*26

for i in range(len(s)):
    j = ord(s[i]) - 65
    alp[j] = alp[j] + 1
 
for i in range(26):
    if alp[i] > 0:
        if alp[i] % 2 == 0:
            e = e + 1
        else:
            o = o + 1

if ((e > 0 and o == 0) or (o == 1)):
    answer = ''

    if o == 1:
        for i in range(26):

            if alp[i] % 2 == 1:
                k = i

            if alp[i] > 1:
                
                for j in range(alp[i]//2):
                    answer = answer + chr(i+65)

        answer = answer + chr(k+65)
        t = answer[:len(answer)-1:]
        answer = answer + t[::-1]
        print(answer)

    if (e > 0 and o == 0):

        for i in range(26):
            if alp[i] > 0:
                
                for j in range(alp[i]//2):
                    answer = answer + chr(i+65)

        answer = answer + answer[::-1]
        print(answer)

else:
    print("I'm Sorry Hansoo")