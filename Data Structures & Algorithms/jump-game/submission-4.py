class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0 
        farthest = nums[0]
        while i < len(nums) and i <= farthest:
            if i == farthest and nums[i] == 0:
                return i == len(nums)-1
            farthest = max(farthest, i + nums[i])
            i+=1
        return i >= len(nums)-1
        
            
        
