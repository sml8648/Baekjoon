import sys
input = sys.stdin.readline

def gear_rotate(gear, direction):
    if direction == -1:
        result = gear[1:] + gear[0]
    elif direction == 1:
        result = gear[-1] + gear[:-1]
    return result

gears = [[0]]
for _ in range(4):
    gears.append(str(input().strip()))

num_rotate = int(input())
for _ in range(num_rotate):

    gear_num, direction = map(int,input().split())

    # 2,6
    if gear_num == 3:
        new_gears = [''] * 5
        new_gears[3] = gear_rotate(gears[gear_num], direction)

        if gears[3][2] != gears[4][6]:
            new_gears[4] = gear_rotate(gears[4], -direction)

        if gears[2][2] != gears[3][6]:
            new_gears[2] = gear_rotate(gears[2], -direction)

            direction = -direction

            if gears[1][2] != gears[2][6]:
                new_gears[1] = gear_rotate(gears[1], -direction)

    if gear_num == 2:
        new_gears = [''] * 5
        new_gears[2] = gear_rotate(gears[gear_num], direction)

        if gears[1][2] != gears[2][6]:
            new_gears[1] = gear_rotate(gears[1], -direction)

        if gears[2][2] != gears[3][6]:
            new_gears[3] = gear_rotate(gears[3], -direction)

            direction = -direction

            if gears[3][2] != gears[4][6]:
                new_gears[4] = gear_rotate(gears[4], -direction)

    if gear_num == 1:
        new_gears = [''] * 5
        new_gears[1] = gear_rotate(gears[gear_num], direction)

        if gears[1][2] != gears[2][6]:
            new_gears[2] = gear_rotate(gears[2], -direction)
            direction = -direction

            if gears[2][2] != gears[3][6]:
                new_gears[3] = gear_rotate(gears[3], -direction)
                direction = -direction

                if gears[3][2] != gears[4][6]:
                    new_gears[4] = gear_rotate(gears[4], -direction)

    if gear_num == 4:
        new_gears = [''] * 5
        new_gears[4] = gear_rotate(gears[gear_num], direction)

        if gears[3][2] != gears[4][6]:
            new_gears[3] = gear_rotate(gears[3], -direction)
            direction = -direction

            if gears[2][2] != gears[3][6]:
                new_gears[2] = gear_rotate(gears[2], -direction)
                direction = -direction

                if gears[1][2] != gears[2][6]:
                    new_gears[1] = gear_rotate(gears[1], -direction)

    for idx, each in enumerate(new_gears):
        if len(each):
            gears[idx] = each

score = 0
for idx, each in enumerate(gears[1:]):
    if each[0] == '1':
        score += 2**(idx)
print(score)