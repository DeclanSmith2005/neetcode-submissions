# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = defaultdict(int)

        def pre(n, skip):
            if not n:
                return 0
            if skip:
                return pre(n.left, False) + pre(n.right, False)
            if (n, skip) in memo:
                return memo[(n, skip)]
            memo[(n, skip)] = max(n.val + pre(n.left, True) + pre(n.right, True), pre(n.left, False) + pre(n.right, False))
            return memo[(n, skip)]
        
        return max(pre(root, False), pre(root, True))