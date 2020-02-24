N = int(input())
answer = []
for k in range(N):
    l = input()
    r = []
    for i in l:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            r.append(i)
        else:
            r.append('s')

    r2 = ''.join(r)
    a = r2.split('s')

    for i in a:
        if i != '':
            answer.append(int(i))

for i in sorted(answer):
    print(i) 
