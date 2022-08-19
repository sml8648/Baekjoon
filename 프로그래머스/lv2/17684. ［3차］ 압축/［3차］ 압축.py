import string
def solution(msg):
    Compress_dict = {k:idx+1 for idx, k in enumerate(string.ascii_uppercase)}
    Compress_set = set(string.ascii_uppercase)
    answer= []
    index = 26
    start = 0

    while start != len(msg):
        end = start

        tmp_result = Compress_dict[msg[start:end+1]]

        while end != len(msg):
            if msg[start:end+1] in Compress_set:
                tmp_result = Compress_dict[msg[start:end+1]]
                end += 1
            else:
                index += 1
                Compress_dict[msg[start:end+1]] = index
                Compress_set.add(msg[start:end+1])
                break

        answer.append(tmp_result)
        start = end
    
    return answer