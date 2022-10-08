import sys
input = sys.stdin.readline

N = int(input())
arr_list = list(map(int,input().split()))

arr_list.sort()
left, right = 0, N -1

result_list = []
cirt = 2e+9+1

while left < right:
    tmp = arr_list[left] + arr_list[right]
    
    if abs(tmp) < cirt:
        cirt = abs(tmp)
        result_list = [arr_list[left], arr_list[right]]
        
    if tmp < 0:
        left +=1
        
    else:
        right -=1
        
print(result_list[0],result_list[1])