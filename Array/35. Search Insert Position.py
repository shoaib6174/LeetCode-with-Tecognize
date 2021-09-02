class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = len(nums)
        for i in range(l):
            val = nums[i]
            if val == target:
                return i
            if val > target:
                return i
            
            
        return l
