from collections import deque

n, l, w = map(int,input().split())
a_list = deque(list(map(int,input().split()))[::-1])
bridge = deque([0]*l)

current_weight = 0
time = 0

while True:

    if time:
        if not sum(bridge):
            break

    time += 1
    #print(bridge)

    c = bridge.popleft()
    bridge.append(0)
    current_weight -= c
    
    if a_list:
        a = a_list.pop()
    else:
        continue
    
    if (current_weight + a) <= w :

        c = bridge.pop()
        bridge.append(a)
        current_weight += a
        current_weight -= c
    else:
        a_list.append(a)

print(time)