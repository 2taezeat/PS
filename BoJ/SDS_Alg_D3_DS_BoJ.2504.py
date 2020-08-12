l1 = list(input())
s = []
current = 1
result = 0
q = 1

for i in range(len(l1)):
    if ((l1[i] == ']') or (l1[i] == ')')) and (s == []):
        q = 0
        break
        
    if l1[i] == '(':
        s.append('(')
        current = current * 2
        if i+1 < len(l1) and l1[i+1] == ')':
            result = result + current
            
    elif l1[i] == '[':
        s.append('[')
        current = current * 3
        if i+1 < len(l1) and l1[i+1] == ']':
            result = result + current    

    if s != []:
        if l1[i] == ')':
            current = current // 2
            if s[-1] == '(':
                s.pop()
                
        elif l1[i] == ']':
            current = current // 3
            if s[-1] == '[':
                s.pop()

if q == 0:
    print(0)

else:
    if s == []:
        print(result)
    else:
        print(0)
