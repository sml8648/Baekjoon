import sys
input = sys.stdin.readline

N = int(input())
arr_list = list(map(int, input().split()))
X = int(input())

arr_list.sort()
left, right = 0, N -1
result = 0

while left < right:
    tmp = arr_list[left] + arr_list[right]
    if tmp == X:
        result += 1
        
    if tmp < X:
        left +=1
    else:
        right -=1
print(result)