class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[]for r in range(numRows)]
        i = r = c = 0
        while i < len(s):
            while i < len(s) and r < numRows-1:
                res[r].append(s[i])
                i+=1; r +=1
            while i < len(s) and r > 0:
                res[r].append(s[i])
                i+=1; r-=1
        return "".join("".join(r) for r in res)