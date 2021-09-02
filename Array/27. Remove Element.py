class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        l = len(nums)
        for i in range(l):
            v = nums[i]
            
            if v != val:
                nums[j] = v
                j += 1 
                
        return j 
            
