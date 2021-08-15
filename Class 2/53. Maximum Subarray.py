class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]
        for n in nums:
            cursum = max(cursum+n,n)
            maxsum = max(maxsum,cursum)
        return maxsum    
        
 # Another Solution
 
 class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = []
        temp = 0
        
        for num in nums:
            temp += num
            if num > temp:
                temp = num
            output.append(temp)
   
        return max(output)
