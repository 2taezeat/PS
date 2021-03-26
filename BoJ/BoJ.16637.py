from itertools import combinations
import math,copy
N = int(input())
eq = list(input())
rmfnq = []
j = 1
for i in range(0,N-1,+2):
    rmfnq.append(j)
    j = j + 1
gnqhrns,chlwhd = [],[]
for i in range(1,(math.ceil(N//2/2)+1)):
    gnqhrns.append(list(combinations(rmfnq, i)))

for c in gnqhrns:
    dpql1 = []
    for p in c:
        pl = len(p)
        if pl == 1:
            dpql1.append(p)
            
        elif pl == 2:
            if p[1] - p[0] > 1 :
                dpql1.append(p)

        elif pl == 3:
                if p[1] - p[0] > 1 and p[2] - p[1] > 1 :
                    dpql1.append(p)

        elif pl == 4:
                if p[1] - p[0] > 1 and p[2] - p[1] > 1 and p[3]-p[2] > 1:
                    dpql1.append(p)

        elif pl == 5:
                if p[1] - p[0] > 1 and p[2] - p[1] > 1 and p[3]-p[2] > 1 and p[4]-p[3] > 1:
                    dpql1.append(p)
    chlwhd.append(dpql1)            

answer = []
for ch in chlwhd:
    for list1 in ch:
        result_eq = []
        if len(list1) == 1:
            n0 = list1[0]
            i = 0
            while(i < N):
                if n0*2-2 <= i <= n0*2:
                    a = "".join(eq[n0*2-2:n0*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                else:
                    result_eq.append(eq[i])
                    i = i + 1                
            
        elif len(list1) == 2:
            n0 = list1[0]
            n1 = list1[1]
            i = 0
            while(i < N):
                if n0*2-2 <= i <= n0*2:
                    a = "".join(eq[n0*2-2:n0*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n1*2-2 <= i <= n1*2:
                    a = "".join(eq[n1*2-2:n1*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                else:
                    result_eq.append(eq[i])
                    i = i + 1

        elif len(list1) == 3:
            n0 = list1[0]
            n1 = list1[1]
            n2 = list1[2]
            i = 0
            while(i < N):
                if n0*2-2 <= i <= n0*2:
                    a = "".join(eq[n0*2-2:n0*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n1*2-2 <= i <= n1*2:
                    a = "".join(eq[n1*2-2:n1*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n2*2-2 <= i <= n2*2:
                    a = "".join(eq[n2*2-2:n2*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                else:
                    result_eq.append(eq[i])
                    i = i + 1
            
        elif len(list1) == 4:
            n0 = list1[0]
            n1 = list1[1]
            n2 = list1[2]
            n3 = list1[3]
            i = 0
            while(i < N):
                if n0*2-2 <= i <= n0*2:
                    a = "".join(eq[n0*2-2:n0*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n1*2-2 <= i <= n1*2:
                    a = "".join(eq[n1*2-2:n1*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n2*2-2 <= i <= n2*2:
                    a = "".join(eq[n2*2-2:n2*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n3*2-2 <= i <= n3*2:
                    a = "".join(eq[n3*2-2:n3*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                else:
                    result_eq.append(eq[i])
                    i = i + 1
            
        elif len(list1) == 5:
            n0 = list1[0]
            n1 = list1[1]
            n2 = list1[2]
            n3 = list1[3]
            n4 = list1[4]
            i = 0
            while(i < N):
                if n0*2-2 <= i <= n0*2:
                    a = "".join(eq[n0*2-2:n0*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n1*2-2 <= i <= n1*2:
                    a = "".join(eq[n1*2-2:n1*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n2*2-2 <= i <= n2*2:
                    a = "".join(eq[n2*2-2:n2*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n3*2-2 <= i <= n3*2:
                    a = "".join(eq[n3*2-2:n3*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                elif n4*2-2 <= i <= n4*2:
                    a = "".join(eq[n4*2-2:n4*2+1])
                    result_eq.append( str(eval(a)))
                    i = i + 3
                else:
                    result_eq.append(eq[i])
                    i = i + 1
        
        s = int(result_eq[0])
        for r in range(1, len(result_eq)-1):
            if result_eq[r] == '+':
                s = s + int(result_eq[r+1])
            elif result_eq[r] == '-':
                s = s - int(result_eq[r+1])
            elif result_eq[r] == '*':
                s = s * int(result_eq[r+1])

        answer.append(s)

if N==1:
    print(eq[0])
else:
    print(max(answer))