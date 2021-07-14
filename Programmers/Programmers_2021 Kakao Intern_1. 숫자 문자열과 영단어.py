def solution(s):
    answer = ""
    i = 0
    while i < len(s):
        if 48 <= ord(s[i]) <= 57:
            answer += s[i]
            i+= 1
            
        elif i < len(s) - 2:
            if s[i] == 'z':
                i += 4
                answer += '0'
            
            elif s[i] == 'e':
                i += 5
                answer += '8'
            
            elif s[i] == 'n':
                i+= 4
                answer += '9'
                
            elif s[i] == 'o':
                i += 3
                answer += '1'
                
            elif s[i] == 't':
                if s[i+1] == 'w':
                    i += 3
                    answer += '2'
                    
                elif s[i+1] == 'h':
                    i += 5
                    answer += '3'
                    
                    
            elif s[i] == 'f':
                if s[i+1] == 'o':
                    i += 4
                    answer += '4'
                    
                elif s[i+1] == 'i':
                    i += 4
                    answer += '5'
                    
            elif s[i] == 's':
                if s[i+1] == 'i':
                    i += 3
                    answer += '6'
                    
                elif s[i+1] == 'e':
                    i += 5
                    answer += '7'
                    
    return int(answer)