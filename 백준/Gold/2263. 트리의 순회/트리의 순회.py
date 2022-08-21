import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

inorder_idx = [0] * (n+1)
for i in range(n):
    inorder_idx[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]

    left_node = inorder_idx[root] - in_start
    right_node = in_end - inorder_idx[root]

    print(root,end=' ')
    preorder(in_start,in_start + left_node - 1, post_start, post_start + left_node - 1)
    preorder(in_end - right_node + 1, in_end, post_end - right_node, post_end - 1)

preorder(0,n-1,0,n-1)