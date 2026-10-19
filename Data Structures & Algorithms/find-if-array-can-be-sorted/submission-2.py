class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # if any contiguous group of values has the same number of setBits, that group can be sorted. if the mins and maxes of each consecutive group are not out of order, then we can produce check
        # for ecah interval need to store, start ind, end ind, min and max
        
        
        def setBits(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n >>= 1
            return count
        
        check = []

        mini, maxi = float('inf'), float('-inf')
        for i in range(len(nums)-1):
            mini, maxi = min(nums[i], mini), max(nums[i], maxi)
            if setBits(nums[i]) != setBits(nums[i+1]):
                check.append((mini, maxi))
                mini, maxi = float('inf'), float('-inf')
        
        mini, maxi = min(nums[-1], mini), max(nums[-1], maxi)
        check.append((mini, maxi))

        
        for i in range(len(check)-1):
            a, b = check[i]
            c, d = check[i+1]
            if b > c:
                return False

        return True




        
