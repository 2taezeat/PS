e, s, m = map(int,input().split())
y = 1
E,S,M = 1,1,1

while(1):
    if (E == e) and (S == s) and (M == m):
        break
    
    E = E + 1
    S = S + 1
    M = M + 1

    if E == 16:
        E = 1

    if S == 29:
        S = 1

    if M == 20:
        M = 1

    y = y + 1

    if (E == e) and (S == s) and (M == m):
        break

print(y)