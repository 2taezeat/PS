def link_check(ll):
    r = []
    al = []
    for l in ll:
        if len(l) > 1:
            r.append(l[0])
            al.append(l[0])
            break

    while(r):
        alpha = r.pop()
        for i in ll[alpha]:
            if i not in al:
                al.append(i)
                r.append(i)
    
    print(al)

link_check([[0, 1, 3], [1, 0, 2], [2, 1], [3, 0]])