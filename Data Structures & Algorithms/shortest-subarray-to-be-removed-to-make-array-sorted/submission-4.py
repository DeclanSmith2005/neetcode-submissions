class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # Find the end of the longest sorted prefix.
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        # Find the start of the longest sorted suffix.
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Keep only the prefix, or keep only the suffix.
        res = min(n - left - 1, right)

        # Try keeping both a prefix and a suffix.
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res