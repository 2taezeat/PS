A, B, C , X ,Y = map(int,input().split())
result = 0

if A+B < 2*C:
    result = A*X + B*Y


else:
    m = min(X, Y)


    if m == Y: # 후라이드가 더 작은 마리수
        result = (m*2*C) + (X-m)*A
        if A > 2*C:
            result = (m*2*C) + (X-m)*2*C

    if m == X: # 양념이 더 작은 마리수
        result = (m*2*C) + (Y-m)*B
        if B> 2*C:
            result = (m*2*C) + (Y-m)*2*C


print(result)