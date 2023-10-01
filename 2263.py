# 이문제는 근야 preorder의 끝을 판단하여 두개의 트리를 구분짓는 걸 찾은다음
# 어떻게 두개가 되는지는 inorder을 이용해서 푸는문제임 ㅇㅇㅇㅇ
import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_parent_lst = [0] * (n + 1)
for i in range(n):
    in_parent_lst[in_order[i]] = i


def find_tree(post_left, post_right, in_left, in_right):
    if post_right < post_left or in_right < in_left:
        return
    parent = post_order[post_right]
    print(parent, end=' ')
    in_parent_idx = in_parent_lst[parent]
    find_tree(post_left, post_left + in_parent_idx - in_left - 1, in_left, in_left + (in_parent_idx - in_left) - 1)
    find_tree(post_right - (in_right - in_parent_idx), post_right - 1, in_right - (in_right - in_parent_idx) + 1,
              in_right)


find_tree(0, n - 1, 0, n - 1)
