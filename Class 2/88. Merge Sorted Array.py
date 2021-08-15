class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            i = m- 1
            j = n -1
            re = min(nums1[0], nums2[0])
            
            p = m + n -1
            
            while p >= 0:
                if i >= 0:
                    val1= nums1[i]
                else:
                    val1 = re
                if j >= 0:
                    val2= nums2[j]
                else:
                    break
                
                if val1 > val2:
                    nums1[p] = val1
                    nums1[i] = re
                    i = i -1
                else:
                    nums1[p] = val2
                    j = j-1
                p -= 1
