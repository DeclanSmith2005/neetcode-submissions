class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # want to keep each value that is smaller than the smallest seen
        # compare each of these to the current guy and get the
        stack = []
        res = 0
        for i, v in enumerate(nums):
            if not stack:
                stack.append((i, v))
                continue
            if v < stack[-1][1]:
                stack.append((i, v))
            else:
                for ind, val in stack:
                    if val <= v:
                        res = max(res, i - ind)
                        break
        return res

