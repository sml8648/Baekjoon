def solution(my_string, num1, num2):
    
    my_string = [each for each in my_string]
    tmp = my_string[num1]
    tmp2 = my_string[num2]
    
    my_string[num1] = tmp2
    my_string[num2] = tmp
    return ''.join(my_string)