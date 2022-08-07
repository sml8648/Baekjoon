import sys
input = sys.stdin.readline
m = int(input())

for i in range(m):
    n,k = map(int,input().split())
    numbers = list(map(int, input().split()))
    answer = [0]

    for number in numbers:
        if answer[-1] < number:
            answer.append(number)
        else:
            left = 0
            right = len(answer)

            while left < right:
                mid = (right+left)//2
                if answer[mid] < number:
                    left = mid+1
                else:
                    right = mid
            answer[right] = number

    print(f'Case #{i+1}')
    result = len(answer) - 1
    if result >= k:
        print(1)
    else:
        print(0)