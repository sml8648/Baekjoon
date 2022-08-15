from itertools import product
import string
from collections import Counter

str_comb = set(map(''.join,product(string.ascii_lowercase,repeat=2)))

def str_combination(str):
    tmp_comb = []
    for a, b in zip(str, str[1:]):
        tmp_str = a + b

        if tmp_str in str_comb:
            tmp_comb.append(tmp_str)

    return tmp_comb


def solution(str1, str2):
    
    Str1 = str1.lower()
    Str2 = str2.lower()
    Str1 = Counter(str_combination(Str1))
    Str2 = Counter(str_combination(Str2))
    
    union = list((Str1 | Str2).elements())
    inter = list((Str1 & Str2).elements())
    
    if len(Str1) == 0 and len(Str2) == 0:
        return 65536
    else:
        return int(len(inter)/len(union)*65536)