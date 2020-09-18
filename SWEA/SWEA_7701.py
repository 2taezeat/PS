t = int(input())

for i in range(t):
    n = int(input()) # 입력받기
    
    l1 = set() # 같은 이름은 하나만 남겨놓기 => set
    for j in range(n):
        c = input()
        l1.add((c,len(c))) # 입력받기

    print("#",end='')
    print(i+1)
    
    l1 = list(l1)
    l1.sort(key = lambda x :(x[1],x[0])) # 이승 명부는 이름의 길이가 짧을수록 이 앞에 있었고, 같은 길이면 사전 순으로 앞에 있었다.
    
    for e in l1:
        print(e[0]) # 정렬후 출력
