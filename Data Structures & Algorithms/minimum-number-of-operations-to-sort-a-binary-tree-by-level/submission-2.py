# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        def numSwaps(arr):
            total = 0
            correct = {v:i for i, v in enumerate(sorted(arr))}
            visited = [0]* len(arr)

            for i in range(len(arr)):
                if visited[i]:
                    continue
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = 1
                    length +=1
                    j = correct[arr[j]]
                total += length -1
            return total



        while q:
            res+= numSwaps([n.val for n in q])
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res