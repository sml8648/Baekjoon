import string

def solution(s, n):
    answer = ''
    for each in s:
        if each == ' ':
            answer += ' '
            continue

        tmp = ord(each) + n
        if each in string.ascii_lowercase:
            if tmp > 122:
                tmp -= 26
        else:
            if tmp > 90:
                tmp -= 26

        answer += chr(tmp)
    
    return answer