from collections import deque

def solution(aa):
    
    maps = aa
    
    n = len(maps) - 1
    m = len(maps[0]) - 1
    
    move = [[-1,0],[0,-1],[1,0],[0,1]]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x,y = q.popleft()

        for a,b in move:
            new_x = x + a
            new_y = y + b
            if 0<= new_x <= n and 0 <= new_y <= m and maps[new_x][new_y] == 1:

                maps[new_x][new_y] = maps[x][y] + 1
                q.append((new_x,new_y))
    
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]