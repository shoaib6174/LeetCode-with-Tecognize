class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        j = 1
        for i in range(1, len(nums)):
            val = nums[i]
            if  val != nums[i-1]:
                nums[j] = val
                j += 1
        
        return j
        
 # Another Solution
 
 class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
