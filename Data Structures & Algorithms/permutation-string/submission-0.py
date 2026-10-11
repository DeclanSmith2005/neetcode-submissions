class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a =Counter(s1)
        b = defaultdict(int)
        l = 0
        for r in range(len(s1)):
            b[s2[r]] += 1
        if a == b:
            return True
        print(a, "rere")
        for r in range(len(s1), len(s2)):
            print(b)
            b[s2[l]] -= 1
            if b[s2[l]] == 0:
                del b[s2[l]]
            l +=1
            b[s2[r]] += 1
            if a == b:
                print(r)
                print(b)
                return True
        return False
