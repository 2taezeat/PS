s = input()
al = ['c=', 'c-', 'd-', 'lj', 'nj', 's=','dz=','z=']

for a in al:
    s = s.replace(a,'#')

print(len(s))

