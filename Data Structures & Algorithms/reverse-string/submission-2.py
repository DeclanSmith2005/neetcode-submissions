class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def switch(a, b):
            tmp  = s[a]
            s[a] = s[b]
            s[b] = tmp
        for i in range(len(s)//2):
            switch(i, -i-1)
        
