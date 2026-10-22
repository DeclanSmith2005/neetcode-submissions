class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = 0 
        l = 0
        res = float('-inf')
        for r, v in enumerate(nums):
            if v == 0:
                zeroCount += 1
            while l < r and zeroCount > k:
                zeroCount += -1 if nums[l] == 0 else 0
                l +=1 
            res = max( res, r - l +1)
        return k if all(i == 0 for i in nums) else res
        

