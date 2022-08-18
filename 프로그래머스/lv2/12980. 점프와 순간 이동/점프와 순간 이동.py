def solution(n):
    
    if n == 1:
        return 1
    
    a = n
    count = 0
    while True:

        if not a % 2:
            a //= 2
        else:
            a -= 1
            count += 1

        if a == 1:
            break

    return count + 1