def solution(l):

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[j].startswith(l[i])) != False or (l[i].startswith(l[j])) != False:
                return False

    return True