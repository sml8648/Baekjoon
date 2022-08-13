def solution(new_id):
    answer = ''
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    check_list = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    for each in new_id:
        if each in check_list:
            answer += each
            
    # step 3
    step3 = ''
    for idx, each in enumerate(answer):
        if idx == 0:
            step3 += each
        else:
            if each == '.':
                if step3[-1] == '.':
                    continue
                else:
                    step3 += each
            else:
                step3 += each
    
    # step 4
    try:
        if step3[0] == '.':
            step3 = step3[1:]
    except:
        step3 = step3
    
    try:
        if step3[-1] == '.':
            step3 = step3[:-1]
    except:
        step3 = step3
    
    # step 5:
    
    if not len(step3):
        step3 += 'a'
    
    # step 6:
    if len(step3) >= 16:
        step3 = step3[:15]
    
    if step3[-1] == '.':
        step3 = step3[:-1]
    
    # step 7:
    if len(step3) <= 2:
        
        tmp = 3 - len(step3)
        step3 += step3[-1]*tmp
        
    return step3