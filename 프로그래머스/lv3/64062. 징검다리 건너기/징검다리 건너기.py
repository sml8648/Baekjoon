def solution(stones, k):

    min_value = min(stones)
    max_value = max(stones)
    result = []
    while min_value <= max_value:

        flag = False
        mid = (min_value + max_value) // 2

        count = 0
        for each in stones:

            if each <= mid:
                count += 1
            else:
                count = 0

            if count == k:
                flag = True
                break

        if flag:
            result.append(mid)
            max_value = mid - 1
        else:
            min_value = mid + 1

    return min(result)