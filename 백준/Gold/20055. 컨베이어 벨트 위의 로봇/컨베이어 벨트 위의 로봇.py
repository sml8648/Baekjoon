import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int,input().split())))
robot = deque([False] * n)
result = 1

while True:
    belt.rotate()
    robot.rotate()
    robot[n - 1] = False

    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] >= 1:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1

    robot[n - 1] = False

    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1

    if belt.count(0) >= k:
        break
    result += 1
print(result)