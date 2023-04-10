from collections import deque

# 변하면 안되는 값들은 tuple로 설정을 해두고
idx = [[0,1,0,1],[1,0,1,0],[-1,0,-1,0],[0,-1,0,-1]]
idx_horiz = [[-1,1,0,0],[1,1,0,0],[0,0,1,-1],[0,0,-1,-1]]
idx_verti = [[1,-1,0,0],[1,1,0,0],[0,0,-1,1],[0,0,-1,-1]]

def rotate_check(board,
                 tx1,ty1,tx2,ty2,
                 n_tx1,n_ty1,n_tx2,n_ty2):

    min_x = min(tx1,tx2,n_tx1, n_tx2)
    min_y = min(ty1,ty2,n_ty1, n_ty2)

    for i in range(min_x,min_x+2):
        for j in range(min_y, min_y+2):
            if board[i][j]:
                return False
    return True

def solution(board):

    x1, y1 = 0,0
    x2, y2 = 0,1
    flag = 'h'
    length = len(board)

    visited = set()
    visited.add((x1,y1,x2,y2))

    q = deque()
    q.append((0, x1, y1, x2, y2, flag))

    while q:
        count, tx1, ty1, tx2, ty2, direct = q.popleft()

        if (tx1 == length -1 and ty1 == length - 1) or (tx2 == length - 1 and ty2 == length - 1):
            return count

        for each in idx:
            n_tx1 = tx1 + each[0]
            n_ty1 = ty1 + each[1]
            n_tx2 = tx2 + each[2]
            n_ty2 = ty2 + each[3]
            new_direct = direct

            coordinate = sorted([(n_tx1, n_ty1), (n_tx2, n_ty2)], key=lambda x: (x[0], x[1]))
            n_tx1, n_ty1, n_tx2, n_ty2 = *coordinate[0], *coordinate[1]

            # 반복되는 체크 로직은 함수로 설정을 해둔다.
            if 0 <= n_tx1 < length and 0 <= n_ty1 < length and 0 <= n_tx2 < length and 0 <= n_ty2 < length \
                and not board[n_tx1][n_ty1] and not board[n_tx2][n_ty2]:

                if (n_tx1, n_ty1, n_tx2, n_ty2) not in visited:
                    q.append((count + 1, n_tx1, n_ty1, n_tx2, n_ty2, new_direct))
                    visited.add((n_tx1, n_ty1, n_tx2, n_ty2))

        if direct == 'h':

            for each in idx_horiz:
                n_tx1 = tx1 + each[0]
                n_ty1 = ty1 + each[1]
                n_tx2 = tx2 + each[2]
                n_ty2 = ty2 + each[3]
                new_direct = 'v'

                coordinate = sorted([(n_tx1, n_ty1), (n_tx2, n_ty2)], key=lambda x: (x[0], x[1]))
                n_tx1, n_ty1, n_tx2, n_ty2 = *coordinate[0], *coordinate[1]

                if 0 <= n_tx1 < length and 0 <= n_ty1 < length and 0 <= n_tx2 < length and 0 <= n_ty2 < length \
                        and rotate_check(board, tx1,ty1,tx2,ty2,n_tx1,n_ty1,n_tx2,n_ty2):

                    if (n_tx1, n_ty1, n_tx2, n_ty2) not in visited:
                        q.append((count + 1, n_tx1, n_ty1, n_tx2, n_ty2, new_direct))
                        visited.add((n_tx1, n_ty1, n_tx2, n_ty2))

        else:

            for each in idx_verti:
                n_tx1 = tx1 + each[0]
                n_ty1 = ty1 + each[1]
                n_tx2 = tx2 + each[2]
                n_ty2 = ty2 + each[3]
                new_direct = 'h'

                coordinate = sorted([(n_tx1, n_ty1), (n_tx2, n_ty2)], key=lambda x: (x[0], x[1]))
                n_tx1, n_ty1, n_tx2, n_ty2 = *coordinate[0], *coordinate[1]

                if 0 <= n_tx1 < length and 0 <= n_ty1 < length and 0 <= n_tx2 < length and 0 <= n_ty2 < length \
                        and rotate_check(board, tx1,ty1,tx2,ty2,n_tx1,n_ty1,n_tx2,n_ty2):

                    if (n_tx1, n_ty1, n_tx2, n_ty2) not in visited:
                        q.append((count + 1, n_tx1, n_ty1, n_tx2, n_ty2, new_direct))
                        visited.add((n_tx1, n_ty1, n_tx2, n_ty2))