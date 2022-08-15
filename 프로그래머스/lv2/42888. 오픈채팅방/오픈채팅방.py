def solution(record):
    message_list = []
    id_name = {}
    for each in record:
        tmp = each.split()
        if tmp[0] != 'Change':
            message_list.append((tmp[0],tmp[1]))

            if tmp[0] == 'Enter':
                id_name[tmp[1]] = tmp[2]
        else:
            id_name[tmp[1]] = tmp[2]

    result_list = []
    for each in message_list:
        if each[0] == 'Enter':
            result_list.append(f"{id_name[each[1]]}님이 들어왔습니다.")
        elif each[0] == 'Leave':
            result_list.append(f"{id_name[each[1]]}님이 나갔습니다.")
    
    return result_list