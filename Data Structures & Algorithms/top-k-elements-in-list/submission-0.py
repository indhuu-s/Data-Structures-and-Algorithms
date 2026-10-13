class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        seen = {} # 1:3,2:2,3:1
        for n in nums:
            seen[n] = seen.get(n,0) + 1
        for n, f in seen.items():
            bucket[f]. append(n)
#buckets = [[], [3], [],[1,2], ],][]]
        for i in range(len(bucket) - 1,- 1,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res











        