from collections import deque
def solution(x, y, n):
    answer = 0
    
    q = deque()
    q.append((x, answer))

    visited = [False]*(y+1)
    
    flag = False
    while q:

        current, count = q.popleft()

        if current == y:
            flag = True
            break

        for idx, each in enumerate([n,2,3]):
            
            # calculate
            if idx == 0:
                new_current = current + n
            else:
                new_current = current * each

            # check whether the value is less than y
            if new_current <= y and not visited[new_current]:
                visited[new_current] = True
                q.append((new_current, count + 1))
    
    if flag:
        return count
    else:
        return -1
                
    
    