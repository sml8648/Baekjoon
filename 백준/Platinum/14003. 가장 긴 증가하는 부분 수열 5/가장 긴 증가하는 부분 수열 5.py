import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

D = [1]*len(numbers)
answer = [-1000000001]

count = 0
for idx, number in enumerate(numbers):
    if answer[-1] < number:
        answer.append(number)

        count += 1
        D[idx] = count

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

        D[idx] = right

print(len(answer)-1)

tmp = len(answer) - 1

result_list = []
for i in range(len(D)-1,-1,-1):

    if D[i] == tmp:
        result_list.append(numbers[i])
        tmp -= 1
        
result_list.sort()
print(*result_list)