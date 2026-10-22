class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = defaultdict(list)
        for i, v in enumerate(numbers):
            mapping[v].append(i)
        
        for i, v in enumerate(numbers):
            for cand in mapping[target-v]:
                if cand > i:
                    return [i+1, cand+1]
        return -1
