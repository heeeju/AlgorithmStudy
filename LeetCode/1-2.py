#4873ms -> 80ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        info = {}
        for idx in range(len(nums)):
            n = target-nums[idx]
            if n not in info:
                info[nums[idx]] = idx
            else:
                return [info[n], idx]
