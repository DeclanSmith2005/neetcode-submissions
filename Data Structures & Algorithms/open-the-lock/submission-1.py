class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        res = 0
        count = 0
        for d in deadends:
            if abs(int(d) - int(target)) == 1:
                count +=1
        if count == 2:
            return -1
        for ind in range(4):
            val = int(target[ind])
            res += min(abs(val - 0), abs(10-val))
        return res


