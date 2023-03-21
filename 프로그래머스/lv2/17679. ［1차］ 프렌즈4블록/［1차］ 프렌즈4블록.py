from collections import deque

def solution(m,n,board):

    newboard = []

    for i in range(n):
        tmp_q = deque()
        for j in range(m):
            tmp_q.append(board[j][i])

        newboard.append(tmp_q)
    total_count = 0
    while True:

        newboard2 = [[True for _ in range(m)] for _ in range(n)]
        flag = False


        for i in range(n):
            for j in range(m):

                current = newboard[i][j]

                try:
                    if current == '1': continue

                    if newboard[i][j + 1] == current and \
                            newboard[i + 1][j] == current and \
                            newboard[i + 1][j + 1] == current:

                        flag = True

                        newboard2[i][j] = False
                        newboard2[i][j+1] = False
                        newboard2[i+1][j] = False
                        newboard2[i+1][j+1] = False
                except:
                    continue

        if not flag: break

        tmp = []
        for i in range(n):
            que = deque()
            false_count = 0
            for j in range(m):

                aa = newboard[i].popleft()

                if not newboard2[i][j]:
                    false_count += 1
                    total_count += 1
                else:
                    que.append(aa)

            for _ in range(false_count):
                que.appendleft('1')

            tmp.append(que)

        newboard = tmp

    return total_count