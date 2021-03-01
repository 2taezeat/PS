for i in range(1000,10000):

    real_i = i
    sum1,sum2,sum3 = 0,0,0 

    while(i>0):
        r1 = i % 10
        q1 = i // 10

        sum1 = sum1 + r1
        i = q1
    
    i = real_i
    while(i>0):
        r2 = i % 12
        q2 = i // 12

        sum2 = sum2 + r2
        i = q2

    i = real_i
    while(i>0):
        r3 = i % 16
        q3 = i // 16

        sum3 = sum3 + r3
        i = q3
    
    if sum1 == sum2 == sum3:
        print(real_i)
