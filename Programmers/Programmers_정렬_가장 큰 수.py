def solution(numbers):
    numbers = list(map(str,numbers))
    semi = []
    for i in numbers:
        semi.append(i*3)
    semi.sort(reverse=True)

    semi2 = []
    ans = ''
    for i in semi:
        k = list(i)
        semi2.append( k[:len(i)//3] )
    
    ans = ''
    for j in semi2:
        for i in j:
            ans = ans + i
    ans = int(ans)
    return str(ans)

print ( solution ([6, 10, 2]) )
print( solution ( [3, 30, 34, 5, 9]) )
print( solution ( [151,15,1]) )
print( solution ( [0,0,0,0]) )
