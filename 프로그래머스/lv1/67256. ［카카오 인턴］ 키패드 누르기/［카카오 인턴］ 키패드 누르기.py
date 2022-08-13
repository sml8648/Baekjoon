def solution(numbers, hand):
    answer = ''
    position_list = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    left_list = set([1,4,7])
    right_list = set([3,6,9])
    
    left_position = position_list[-2]
    right_position = position_list[-1]
    
    for each in numbers:
        
        if each in left_list:
            answer += 'L'
            left_position = position_list[each]
        elif each in right_list:
            answer += 'R'
            right_position = position_list[each]
        else:
            tmp = position_list[each]
            
            left_dist = abs(tmp[0] - left_position[0]) + abs(tmp[1] - left_position[1])
            right_dist = abs(tmp[0] - right_position[0]) + abs(tmp[1] - right_position[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_position = position_list[each]
            elif left_dist > right_dist:
                answer += 'R'
                right_position = position_list[each]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_position = position_list[each]
                else:
                    answer += 'L'
                    left_position = position_list[each]

    return answer