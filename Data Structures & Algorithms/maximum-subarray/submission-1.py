class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = float('-inf')
        res = float('-inf')
        for num in nums:
            if curr < 0:
                curr = num
            else:
                curr += num
            res= max(res, curr)
        
        return res