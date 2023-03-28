def solution(survey, choices):

    character_dict = {each:0 for each in ['R','T','C','F','J','M','A','N']}

    for each, score in zip(survey, choices):

        left = each[0]
        right = each[1]

        if score > 4:
            character_dict[right] += (score - 4)
        elif score < 4:
            character_dict[left] += (4 - score)

    result = ''
    if character_dict['R'] < character_dict['T']:
        result += 'T'
    else:
        result += 'R'

    if character_dict['C'] < character_dict['F']:
        result += 'F'
    else:
        result += 'C'

    if character_dict['J'] < character_dict['M']:
        result += 'M'
    else:
        result += 'J'

    if character_dict['A'] < character_dict['N']:
        result += 'N'
    else:
        result += 'A'

    return result