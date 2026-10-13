class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def rc(curr, ind):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(ind+1, n+1):
                rc(curr + [i], i )
            
        rc([], 0)
        return res