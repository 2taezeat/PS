from collections import Counter
r,c,k = map(int,input().split())
r = r - 1
c = c - 1
A_list = []
for i in range(3):
    A_list.append(list(map(int,input().split())))

def check():
    global A_list
    try:
        if A_list[r][c] == k:
            return True
        else:
            return False
    except:
        return False

def zero_plus():
    global A_list
    max_len = 0
    for a in A_list:
        max_len = max(len(a),max_len)
    
    for a in A_list:
        len_diff = max_len - len(a)
        for _ in range(len_diff):
            a.append(0)

def rotate_90(space):
    list_of_tuples = zip(*space[::-1])
    return [list(elem) for elem in list_of_tuples]

def R_op():
    global A_list
    for a in range(len(A_list)):
        l1 = []
        count_dict = Counter(A_list[a])
        del count_dict[0]
        for c in count_dict:
            l1.append([c, count_dict[c]])
        
        l1.sort(key= lambda x: ( x[1],x[0] ) )
        l2 = []
        for l in l1:
            l2.append(l[0])
            l2.append(l[1])
        A_list[a] = l2

def over_100_cal():
    global A_list
    len_a = len(A_list[0])
    return (len_a - 100)

def C_op():
    global A_list
    A_list = rotate_90(A_list)
    R_op()

def what_op():
    global A_list
    if len( A_list ) >= len( A_list[0] ):
        return 'R'
    else:
        return 'C'

q = 0
for time in range(0,101):
    if check():
        print(time)
        q = 1
        break
    else:
        op = what_op()

        if op == 'R':
            R_op()
            zero_plus()

            o_num = over_100_cal()
            if o_num > 0:
                for a in A_list:
                    for _ in range(o_num):
                        a.pop()

        elif op == 'C':
            C_op()
            zero_plus()

            o_num = over_100_cal()
            if o_num > 0:
                for a in A_list:
                    for _ in range(o_num):
                        a.pop()

            A_list = A_list[::-1]
            A_list = rotate_90(A_list)

if q == 0:
    print(-1)