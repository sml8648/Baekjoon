import heapq

def solution(scoville, K):
    
    new_sc = scoville
    q = []
    count = 0
    
    for i in new_sc:
        heapq.heappush(q,i)
        
    while True:
        
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        
        index = a + b*2
        heapq.heappush(q,index)
        count += 1
        
        tmp = heapq.heappop(q)
        heapq.heappush(q,tmp)
        
        if tmp >= K:
            break
        
        if len(q) == 1:
            count = -1
            break
        
    return count