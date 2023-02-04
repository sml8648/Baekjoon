import sys
input = sys.stdin.readline
import copy

t = int(input())

result = []
def backtracking(i):

    global s

    if i == n:
        s += str(i)
        tmp = copy.deepcopy(s)
        tmp = tmp.replace(' ','')
        if eval(tmp) == 0:
            result.append(s)
        s = s[:-1]
        return

    s += str(i)

    for each in [' ','+','-']:
        s += each
        backtracking(i+1)
        s = s[:-1]

    s = s[:-1]


for _ in range(t):
    n = int(input())
    s = ''
    backtracking(1)
    result.append('')

for each in result:
    print(each)