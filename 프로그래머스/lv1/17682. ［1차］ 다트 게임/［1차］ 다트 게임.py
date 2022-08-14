def solution(a_list):
    bonus = ['S','D','T']
    bonus_dict = {'S':1,'D':2,'T':3}
    option = ['*','#']
    digit_list = ['0','1','2','3','4','5','6','7','8','9','A']
    a_list = a_list.replace('10','A')
    
    result_list = []
    for a, b in zip(a_list,a_list[1:]):
        
        if a in digit_list and b in bonus:
            
            if a == 'A':
                a = 10
                
            tmp = int(a)**bonus_dict[b]
            result_list.append(tmp)
        
        elif b in option:
            if b == '*':
                
                if len(result_list) == 1:
                    result_list[-1] *= 2
                else:
                    result_list[-1] *= 2
                    result_list[-2] *= 2
            else:
                result_list[-1] = -result_list[-1]
    
    print(result_list)
    return sum(result_list)
                    