def solution(board, skill):

    new_board = [[0]*(len(board[0]) + 1) for _ in range(len(board)+1)]

    for each in skill:

        direct, x1, y1, x2, y2, degree = each

        if direct == 1: degree = -degree

        X1, Y1 = x1,y1
        X2, Y2 = x2+1,y1
        X3, Y3 = x1, y2+1
        X4, Y4 = x2+1, y2+1

        new_board[X1][Y1] += degree
        new_board[X2][Y2] += -degree
        new_board[X3][Y3] += -degree
        new_board[X4][Y4] += degree

    before = 0
    for j in range(len(board[0])+1):
        for i in range(len(board)+1):
            new_board[i][j] = new_board[i][j] + before
            before = new_board[i][j]

    before = 0
    for i in range(len(board)+1):
        for j in range(len(board[0])+1):
            new_board[i][j] = new_board[i][j] + before
            before = new_board[i][j]

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + new_board[i][j] > 0: count += 1

    return count
        
        