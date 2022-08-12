import math
def solution(arr):
    answer = (arr[0]*arr[1])//math.gcd(arr[0],arr[1])
    
    for each in arr[2:]:
        
        answer = (answer*each) // math.gcd(answer,each)
        
    return answer