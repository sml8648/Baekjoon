count = 0
result_list = []

def hanoi(n,start,target):

    if n == 0: return

    list = set([1,2,3])
    input_list = set([start,target])
    new_target = list - input_list
    new_target = new_target.pop()

    hanoi(n-1,start,new_target)
    global result_list
    result_list.append([start,target])
    global count
    count+=1
    hanoi(n-1,new_target,target)
    
def solution(n):
    answer = [[]]
    
    hanoi(n,1,3)
    
    return result_list