def check_correct(s):
    
    stack = [0]
    for each in s:
        if each == '(' or each == '{' or each == '[':
            stack.append(each)
        elif each == ')':
            if stack[-1] == '(':
                stack.pop()
            else: return False
        elif each == '}':
            if stack[-1] == '{':
                stack.pop()
            else: return False
        elif each == ']':
            if stack[-1] == '[':
                stack.pop()
            else: return False
    
    return True if len(stack) == 1 else False
    
def solution(s):
    
    count = 0
    rotate = 0
    while rotate != len(s):
        if check_correct(s): count += 1
        
        s = s[-1] + s[:-1]
        rotate += 1
    
    return count