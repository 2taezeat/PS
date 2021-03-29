import collections, itertools, copy
N, M, K = map(int,input().split())
o_space = collections.deque()
trans_list = []
for i in range(N):
    a = list(map(int,input().split()))
    b = collections.deque(a)
    o_space.append(b)
for _ in range(K):
    trans_list.append(list(map(int,input().split())))
per_list = list( itertools.permutations(trans_list) )
answer_list = []
def cal(space):
    result_list = []
    for i in range(N):
        result_list.append(sum(space[i]))
    return min(result_list)

def transition(space, r,c,s):
    lh_y, lh_x = r-s-1, c-s-1
    rl_y, rl_x = r+s-1, c+s-1
    ite_count = (rl_x - lh_x) // 2
    standard = [ ]
    for i in range(0, ite_count):
        left = (lh_y+i, lh_x+i)
        right = (rl_y-i, rl_x-i)
        standard.append((left,right))

    for ss in standard:
        ly,lx, ry,rx = ss[0][0], ss[0][1], ss[1][0], ss[1][1]
        l1,l2,l3,l4 = [], [], [], []

        for i in range(lx, rx):
            l1.append(space[ly][i])
        for i in range(ly, ry):
            l2.append(space[i][rx])
        for i in range(rx,lx,-1):
            l3.append(space[ry][i])
        for i in range(ry,ly,-1):
            l4.append(space[i][lx])

        for i in range(len(l1)):
            space[ly][lx+1+i] = l1[i]
        for i in range(len(l2)):
            space[ly+1+i][rx] = l2[i]
        for i in range(len(l1)):
            space[ry][rx-1-i] = l3[i]
        for i in range(len(l2)):
            space[ry-1-i][lx] = l4[i]
            

    return space



for p in per_list:
    n_space = copy.deepcopy(o_space)
    for R,C,S in p:
        n_space = transition(n_space, R,C,S)

    answer_list.append(cal(n_space))

print(min(answer_list))