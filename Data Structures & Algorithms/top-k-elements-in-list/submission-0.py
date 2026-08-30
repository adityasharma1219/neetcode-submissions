class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        result = []
        for i in range(k):
            max_num = None
            max_count = -1
            for num in counts:
                if counts[num] > max_count:
                    max_count = counts[num]
                    max_num = num
            result.append(max_num)
            del counts[max_num]

        return result