def prime_check(n):
    if n == 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        
        return True

t = int(input())
for i in range(1,t+1):
    a,b = map(int,input().split())
    ### 소수 판별
    if prime_check(b) == False:
        print(a,b,"NO")
        continue
    else:
        pass
    
    bool1 = False
    count = 1
    n = b
    ######################################### 
    while(True):
        sum1 = 0
        n = str(n)

        for d in n:
            sum1 = sum1 + int(d)**2
 
        if sum1 == 1:
            bool1 = True
            break
        count = count + 1
        
        if count > 999:
            break
        n = sum1
    ##########################################
    if bool1 == True:
        print(a,b,"YES")
    else:
        print(a,b,"NO")
