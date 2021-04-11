N, K = map(int,input().split())
space_color = []
dy = [99,0,0,-1,1]
dx = [99,1,-1,0,0]
for i in range(N):
    space_color.append( list ( map(int,input().split()) ) )

print(space_color)

location = []
akf = [[[] * N for i in range(N)] for i in range(N)] 
for i in range(1,K+1):
    y,x,d = map(int,input().split())
    akf[y-1][x-1].append( [i,d] )
    location.append( [i,d,y-1,x-1])

print(akf)



for turn in range(1,3):
    
    ll = []
    for b in range(N):
        for a in range(N):
            l = []
            info = akf[b][a]
            if len( info ) == K:
                break

            if 0 < len( info ) < K:
                info.append(b,a)
                ll.append(info)


    print(ll)
    ll.sort()

    for l in ll:
        
            









print(turn)