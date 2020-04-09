n = int(input())
p = 0
if n % 4 == 0 :
    if n % 100 != 0 or n % 400 ==0:
            p = 1
    
print(p)