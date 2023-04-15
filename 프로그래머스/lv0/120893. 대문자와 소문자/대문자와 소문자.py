def solution(my_string):
    answer = ''
    for each in my_string:
        if each.islower():
            answer += each.upper()
        elif each.isupper():
            answer += each.lower()
    return answer