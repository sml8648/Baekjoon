from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    a_dict = defaultdict(object)
    a_dict = defaultdict(lambda : set())
    
    for each in report:
        a,b = each.split(' ')
        a_dict[a].add(b)

    count_dict = defaultdict(object)
    count_dict = defaultdict(lambda : 0)
    
    a_list = set()
    for _,v in a_dict.items():
        
        for each in v:
            count_dict[each] += 1
            if count_dict[each] >= k:
                a_list.add(each)
    
    final_dict = {}
    for each in id_list:
        final_dict[each] = 0
    
    for each in id_list:
        
        for i in a_dict[each]:
            if i in a_list:
                #print(final_dict[each],each)
                final_dict[each] += 1


    return list(final_dict.values())