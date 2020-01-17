# def cal(num, i):
#     if (num == 1):
#         return (i)

#     if (num % 3 == 0):
#         return cal(num / 3, i + 1)

#     if (num % 2 == 0):
#         if ( ((num-1)/3) % 3 == 0 ):
#             return cal(num - 1, i + 1)
#         else:
#             return cal(num / 2, i + 1)

#     else:
#         return cal(num - 1, i + 1)
N = int(input())

dplist = [0,0,1,1]

for i in range(4,N+1):
    dplist.append( dplist[i-1] + 1 )
    
    if (i % 3 ==0):
        dplist[i] = min(dplist[i], dplist[i//3]+1 )

    if (i % 2 ==0):
        dplist[i] = min(dplist[i], dplist[i//2]+1 ) 

print(dplist[N])

