def solution(board, moves):
    answer = 0
    new_board = list(map(list,zip(*board)))
    
    bucket = []

    for each in moves:
        
        for idx,k in enumerate(new_board[each-1]):
            
            if k:
                if len(bucket) > 0:
                    if bucket[-1] == k:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(k)
                else:
                    bucket.append(k)
                    
                new_board[each-1][idx] = 0
                break
    
    return answer