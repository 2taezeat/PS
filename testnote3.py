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

print(semi)

