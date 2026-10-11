class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
            if counts[nums[i]] > len(nums)// 2:
                return nums[i]