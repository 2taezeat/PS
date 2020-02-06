N, X = map(int,input().split())
lenlist = [1]
list2 = [1] # 패티 갯수
for i in range(1,51):
    list2.append( list2[i-1]*2 + 1 )
    lenlist.append( 3 + ( lenlist[i-1] ) * 2) 

def asd(n, x, llist, plist):
    # for i in range(1,51):

    #     if x <= llist[i]:
    #         if x <= llist[i-1] + 1 :
    #             result = plist[i-1]
    #             result = asd(x-1,n-1,llist,plist)
    #             break

    #         if x == llist[i-1] + 2 :
    #             result = plist[i-1] + 1
    #             break

    #         if llist[i-1] + (i+1) >= x > llist[i-1] + 2:
    #             result = plist[i-1] + 1
    #             break

    #         if x == 2*llist[i-1] + 3:
    #             result = plist[i]
    #             break

    #         if 2*llist[i-1] + 3 > x > llist[i-1] + (i+1):
    #             # d = x - (llist[i-1] + 2 + 1 + i-3)
    #             # #print('d',d)
    #             # if d >= 5 + 1:
    #             #     d = d + 1
    #             #     result = (plist[i-1] + 1) + asd(d,llist,plist)
    #             # else:
    #             #     result = (plist[i-1] + 1) + asd(d,llist,plist) 
    #             # break
                
    #             k = X - ((llist[i]+1 ) // 2 ) + i - 2
    #             result = asd(k,llist,plist) + 1 + plist[i-1]
    #             break
    if n == 0:
        if x == 1:
            return 1
    

    if (x==1):
        return 0
    else:
        if x <= llist[n-1] + 1 :
            return asd(n-1,x-1,llist,plist)
            
        if x == llist[n-1] + 2 :
            return plist[n-1] + 1
            
        if x <= 1 + llist[n-1] + 1 + llist[n-1] :
            return 1 + plist[n-1] + asd(n-1, x-1-llist[n-1]-1 , llist ,plist )

        if x == llist[n-1] * 2 + 3:
            return plist[n-1] * 2 + 1

r = asd(N,X,lenlist,list2)

print(r)
