expression = "100-200*300-500+20"
expression = list(expression)

semi = []
a = ''
for e in range(len(expression)):
    char = expression[e]
    if not (char == '-' or char == '+' or char == '*'):
        a = a + char
    else:
        semi.append(int(a))
        semi.append(char)
        a = ''

semi.append(int(a))
i = 0
while(1):
    if semi[i] == '*':
        left = i
        right = i
        while(1):
            if left == 0:
                break
            if semi[left] == '+' or semi[left] == '-':
                break
            left = left - 1
        
        while(1):
            if right == len(semi):
                break
            if semi[right] == '+' or semi[right] == '-':
                break
            right = right + 1
        

        r = semi[left+1] * semi[right-1]
        del semi[left+1:right]
        i = left
        semi.insert(left+1,r)
        print(semi,i)

    i += 1

    if i >= len(semi):
        break