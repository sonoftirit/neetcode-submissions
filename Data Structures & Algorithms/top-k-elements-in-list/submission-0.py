class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for n in nums:
            result[n] = result.get(n,0) + 1

        #sort number based on their frequencies 
        numbers = sorted(result, key=result.get, reverse=True)
        return numbers[:k]
        