arr = [[0,1,2],[3,4,5],[6,7,8]]
result = list(zip(*arr[::-1])) # 우측 90도
result2 = list(zip(*arr))[::-1] # 좌측 90도
print(result)
print(result2)