a_list = "1T2D3D#"
def solution(a_list):
    bonus = ['S','D','T']
    bonus_dict = {'S':1,'D':2,'T':3}
    option = ['*','#']

    result_list =[]
    for a,b in zip(a_list, a_list[1:]):

        if a.isdigit() and (b in bonus):
            tmp = int(a)**bonus_dict[b]
            result_list.append(tmp)
            print(result_list)
        elif a.isdigit() and 
        elif b in option:
            if b == '*':
                try:
                    result_list[-1] *= 2
                    result_list[-2] *= 2
                except:
                    result_list[-1] *= 2
            else:
                result_list[-1] = -result_list[-1]

    print(result_list)
solution(a_list)