def solution(n):
    a_list = [i+1 for i in range(n)]

    start = 0
    end = 0

    count = 0

    while start != len(a_list):

        tmp_sum = sum(a_list[start:end])

        if tmp_sum < n:
            end += 1
        elif tmp_sum > n:
            start += 1
        else:
            count += 1
            start += 1
            
    return count