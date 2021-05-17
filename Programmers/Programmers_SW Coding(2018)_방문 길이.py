def solution(dirs):
    answer = 0
    y,x = 5,5
    visit = set()

    for d in dirs:
        if d == 'U':
            ny = y - 1
            nx = x
            if 0<= ny <= 10 and 0 <= nx <= 10:
                if (y,x,ny,nx) not in visit:
                    visit.add((y,x,ny,nx))
                    visit.add((ny,nx,y,x))
                    answer += 1
                y = ny
                x = nx

        elif d == 'D':
            ny = y + 1
            nx = x
            if 0<= ny <= 10 and 0 <= nx <= 10:
                if (y,x,ny,nx) not in visit:
                    visit.add((y,x,ny,nx))
                    visit.add((ny,nx,y,x))
                    answer += 1
                y = ny
                x = nx

        elif d == 'R':
            ny = y
            nx = x + 1
            if 0<= ny <= 10 and 0 <= nx <= 10:
                if (y,x,ny,nx) not in visit:
                    visit.add((y,x,ny,nx))
                    visit.add((ny,nx,y,x))
                    answer += 1
                y = ny
                x = nx

        elif d == 'L':
            ny = y
            nx = x - 1
            if 0<= ny <= 10 and 0 <= nx <= 10:
                if (y,x,ny,nx) not in visit:
                    visit.add((y,x,ny,nx))
                    visit.add((ny,nx,y,x))
                    answer += 1
                y = ny
                x = nx

    return answer

print(solution("ULURRDLLU"))