def solution(user_id, banned_id):

    target_list = []
    for each in banned_id:

        result = []
        for k in user_id:

            if len(each) != len(k): continue

            tmp1 = ''
            tmp2 = ''
            for a,b in zip(each, k):

                if a == '*': continue
                tmp1 += a
                tmp2 += b

            if tmp1 == tmp2:
                result.append(k)

        target_list.append(result)

    remove_dup = set()

    s = set()

    final_result = []
    def backtracking(target_list,idx):

        if len(s) == len(banned_id):
            final_result.append(list(s))
            return

        for each in target_list[idx]:

            if each not in s:
                s.add(each)
                backtracking(target_list, idx+1)
                s.remove(each)

    backtracking(target_list,0)

    real_result = set()
    for each in final_result:
        tmp = ''.join(sorted(each))
        real_result.add(tmp)

    return len(real_result)