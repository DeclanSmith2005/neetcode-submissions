# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # try placing any node allowed by the preorder and then if it doesn't agree with in order go next? 
        pos = {val: i for i, val in enumerate(inorder)}
        def build(l, r, root):
            if l > r:
                return None
            mid = pos[preorder[root]]
            left_size = mid - l
            left = build(l, mid - 1, root + 1)
            right = build(mid + 1, r, root + 1 + left_size)

            return TreeNode(preorder[root], left, right)

        return build(0, len(inorder) - 1, 0)