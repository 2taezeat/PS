n,c = map(int,input().split())
l1 = []
for i in range(n):
    l1.append(int(input()))

l1.sort()

start = l1[1] - l1[0] # 집의 좌표 중에 가장 작은 값
end = l1[-1] - l1[0] # 집의 좌쵸중에 가장 큰 값 
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = l1[0]
    count = 1

    print(start,end,mid,count)

    for i in range(1,n): # 앞에서 부터 차근차근 설치
        if l1[i] >= value + mid: 
            value = l1[i]
            count = count + 1


    if count >= c: # c개 이상의 공유기를 설치 할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장

    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리(gap)을 감소
        end = mid -1 


print(result)