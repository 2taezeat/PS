rl = []
for i in range(10):
    rl.append(int(input()) % 42)
srl = set(rl)
print(len(srl))