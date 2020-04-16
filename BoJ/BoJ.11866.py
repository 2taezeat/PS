n , k = map(int,input().split())
l = []
for i in range(1,n+1):
    l.append(i)
answer = []
r = (k-1)
while(l!=[]):
    if r >= len(l):
        while(r >= len(l)):
            r = r - len(l) 
            
        answer.append(l.pop(r))
        r = r +(k-1)

    else:
        answer.append(l.pop(r))
        r = r + (k-1)

print('<',end='') 
for i in range(len(answer)):
    if i == n-1:
        print(answer[i],end='')
    else:
        print("%d, " %(answer[i]) ,end='')

print('>',end='') 