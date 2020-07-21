s = input()
s = list(s)
r = 0
for i in range(len(s)):
    o = ord(s[i])
    
    if 65 <= o <= 67:
        r = r + 3
    elif 68 <= o <= 70:
        r = r + 4
    elif 71 <= o <= 73:
        r = r + 5
    elif 74 <= o <= 76:
        r = r + 6
    elif 77 <= o <= 79:
        r = r + 7
    elif 80 <= o <= 83:
        r = r + 8
    elif 84 <= o <= 86:
        r = r + 9
    elif 87 <= o <= 90:
        r = r + 10

print(r)
    