n = int(input())

a = 0
if n % 8 == 5:
    a = 5
elif n % 8 == 1:
    a = 1
elif n % 4 == 3:
    a = 3
elif (n+2) % 8 == 0 or n % 8 == 4:
    a = 4
elif n % 8 == 2 or n % 8 == 0 :
    a = 2

print(a)