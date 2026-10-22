class Solution:
    def reverseOddLevels(self, root):

        def post(a, b, level):
            if not a:
                return

            if level % 2 == 0:
                a.val, b.val = b.val, a.val

            post(a.left, b.right, level + 1)
            post(a.right, b.left, level + 1)

        post(root.left, root.right, 0)
        return root