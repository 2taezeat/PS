N = int(input())
arr1 = list(map(int,input().split()))
stack = [[0,arr1[0]]]
r = [0] * N
for i in range(1,len(arr1)):
    if arr1[i-1] >= arr1[i]:
        stack.append([i,arr1[i]])
        r[i] = i
        
    else:
        k = len(stack)
        k = k - 1
        while(k > -1):
            if stack[k][1] >= arr1[i]:
                r[i] = (stack[k][0]+1)
                break
            else:
                stack.pop()
            k = k - 1
        
        stack.append([i,arr1[i]])

for i in r:
    print(i, end= ' ')