import sys
import heapq
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())

    arr_list = []
    for _ in range((m // 10) + 1):
        arr_list.extend(list(map(int,input().split())))

    result = [arr_list[0]]
    stack_left = []
    stack_right = []
    middle = arr_list[0]

    for idx, each in enumerate(arr_list[1:]):

        if each >= middle:
            heapq.heappush(stack_right, each)
        elif each < middle:
            heapq.heappush(stack_left, -each)
        
        # 홀 수 일떄
        if idx % 2:
            if len(stack_left) > len(stack_right):
                number = heapq.heappop(stack_left)
                heapq.heappush(stack_right, middle)
                middle = -number
                result.append(middle)

            elif len(stack_left) < len(stack_right):

                number = heapq.heappop(stack_right)
                heapq.heappush(stack_left, -middle)
                middle = number
                result.append(middle)
            else:
                result.append(middle)

    print(len(result))
    for i in range((len(result) // 10) + 1):

        for each in result[i*10:(i+1)*10]:
            print(each, end=' ')
        print()
