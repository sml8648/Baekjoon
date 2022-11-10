point = []
for _ in range(3):
    point.append(list(map(int, input().split())))

tmp = point[0][0]*point[1][1] + point[1][0]*point[2][1] + point[2][0]*point[0][1]
result = tmp - point[1][0]*point[0][1] - point[2][0]*point[1][1] - point[0][0]*point[2][1]

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)