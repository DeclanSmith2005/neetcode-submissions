class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        cost = {}
        curr = 0
        s = sorted([(v, k) for k, v in count.items()], reverse = True)
        i = 0 
        while len(cost) < len(count):
            if i % 8 == 0:
                curr += 1
            cost[s[i][1]] = curr
            i+=1

        print(s, cost)
        
        res = 0
        for l in word:
            res += cost[l]
        return res
