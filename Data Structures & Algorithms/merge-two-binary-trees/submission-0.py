# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inOrder(n1, n2):
            if not n1 and not n2:
                return None
            if not n1:
                return n2
            if not n2:
                return n1
            curr = TreeNode(n1.val + n2.val)
            curr.left = inOrder(n1.left, n2.left)
            curr.right = inOrder(n1.right, n2.right)
            return curr
        
        return inOrder(root1, root2)