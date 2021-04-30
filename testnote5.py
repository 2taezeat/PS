from collections import defaultdict
string_list = ['A','B','C','A']
int_list = [1, 2, 3, 10]
l1 = list(zip(string_list, int_list))

dic1 = defaultdict(int)
for (a,b) in l1:
    dic1[a] = dic1[a] + b

print(dic1)