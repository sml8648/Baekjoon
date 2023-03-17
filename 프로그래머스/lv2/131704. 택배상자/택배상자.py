def solution(order):

    answer = 0
    current = 0
    sub_container = []
    sub_pointer = 1
    for each in order:
        
        if current < each:
            
            for k in range(sub_pointer, each):
                sub_container.append(k)

            sub_pointer = each+1

            current = each
            answer += 1

        else:

            if sub_container[-1] == each:
                sub_container.pop()
                answer += 1
            else:
                return answer

    return answer