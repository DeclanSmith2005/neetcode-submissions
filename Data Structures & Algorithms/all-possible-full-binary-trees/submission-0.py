class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # at each node, can produce children or not. Need to return the node that has children and the node that does not
        if n % 2 == 0:
            return []
    
        memo  ={}
        def dfs(n):
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            res = []
            for i in range(1, n-1, 2):
                l = dfs(i)
                r = dfs(n-1-i)
                for ln in l:
                    for rn in r:
                        res.append(TreeNode(0, ln, rn))
            memo[n] = res
            return res
        
        return dfs(n)
        
            
