#import pprint
from collections import deque
#board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
#board = [".D.R", "....", ".G..", "...D"]

def find_d(board, x, y, each):

    new_x, new_y = x, y

    while True:

        new_x += each[0]
        new_y += each[1]

        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
            if board[new_x][new_y] == "D":
                new_x -= each[0]
                new_y -= each[1]
                break
            else:
                continue

        else:
            new_x -= each[0]
            new_y -= each[1]
            break

    return new_x, new_y

def solution(board):

    start = (0,0)
    goal = (0,0)
    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == 'R': start = i,j
            elif board[i][j] == 'G': goal = i,j

    visited = set()

    q = deque()
    q.append((0, start))

    while q:

        count, (x, y) = q.popleft()
        if count == 100:
            count = -1
            break
        if x == goal[0] and y == goal[1]:
            break

        for each in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

            new_x, new_y = find_d(board, x, y, each)

            if new_x == x and new_y == y: continue

            if (count + 1, new_x, new_y) not in visited:
                q.append((count + 1, (new_x, new_y)))
                visited.add((count + 1, new_x, new_y))

    return count