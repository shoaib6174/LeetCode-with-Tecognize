class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = dict()
        for i, n in enumerate(nums):
            need = target - n
            k = x.get(need)
            if k is not None and k != i:
                return[i,k]
            x[n] = i
