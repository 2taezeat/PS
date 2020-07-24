while(1):
    pl = input()

    if pl == '.':
        break

    pl = list(pl)
    stack = []
    c = 1
    for p in pl:

        if p == '(':
            stack.append(0)
        elif p == '[':
            stack.append(1)

        elif p == ')':
            if len(stack) == 0:
                c = 0
                break

            if stack.pop() != 0:
                c = 0
                break

        elif p == ']':
            if len(stack) == 0: # 0 = '('
                c = 0
                break
            
            if stack.pop() != 1: # 1 = '['
                c = 0
                break


    if len(stack) == 0 and c == 1:
        print('yes')
    else:
        print('no')
