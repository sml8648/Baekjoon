import heapq

def solution(food_times, k):


    q = []
    for idx, each in enumerate(food_times):
        heapq.heappush(q,(each, idx))

    before = 0
    length = len(q)
    answer = -1
    while q:
        food_time, idx = heapq.heappop(q)
        tmp = (food_time - before)*length

        if k >= tmp:
            k -= tmp
            before = food_time
            length -= 1

        else:
            heapq.heappush(q, (food_time,idx))
            result = sorted(q, key=lambda x:x[1])
            index = k % length
            answer = result[index][1] + 1
            break
    
    return answer