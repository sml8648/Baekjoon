import heapq
def solution(n, k, cmds):

    upper_heap = []
    lower_heap = []
    point = -1
    for i in range(n):
        if i < k: heapq.heappush(upper_heap,-i)
        elif i == k: point = k
        else: heapq.heappush(lower_heap,i)

    removed = []

    for cmd in cmds:
        cmd = cmd.split()

        if cmd[0] == 'D':
            move = int(cmd[1])
            heapq.heappush(upper_heap, -point)
            for i in range(move):
                if i == (move-1):
                    point = heapq.heappop(lower_heap)
                else:
                    heapq.heappush(upper_heap, -heapq.heappop(lower_heap))

        elif cmd[0] == 'C':
            removed.append(point)
            if not len(upper_heap):
                point = heapq.heappop(lower_heap)
            elif not len(lower_heap):
                point = -heapq.heappop(upper_heap)
            else:
                point = heapq.heappop(lower_heap)

        elif cmd[0] == 'U':

            move = int(cmd[1])
            heapq.heappush(lower_heap, point)
            for i in range(move):
                if i == (move - 1):
                    point = -heapq.heappop(upper_heap)
                else:
                    heapq.heappush(lower_heap, -heapq.heappop(upper_heap))

        elif cmd[0] == 'Z':
            tobe_add = removed.pop()

            if tobe_add < point:
                heapq.heappush(upper_heap, -tobe_add)
            else:
                heapq.heappush(lower_heap, tobe_add)

    result = ['X']*n

    while upper_heap:
        tmp = -heapq.heappop(upper_heap)
        result[tmp] = 'O'
    result[point] = 'O'
    while lower_heap:
        tmp = heapq.heappop(lower_heap)
        result[tmp] = 'O'

    return ''.join(result)