from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

result_list = []

while True:
    try:
        a = int(input())
        result_list.append(a)
    except:
        break


last_result = []
def post_order(result_list):

    if not len(result_list):
        return

    root = result_list[0]

    right_point = bisect_right(result_list,root)
    right_end = len(result_list)

    left_point = 1
    left_end = right_point

    left_list = result_list[left_point:left_end]
    right_list = result_list[right_point:right_end]

    last_result.append(root)

    post_order(right_list)
    post_order(left_list)

post_order(result_list)

for each in last_result[::-1]:
    print(each)