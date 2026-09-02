class Solution(object):
    
        
    def twoSum(self, nums, target):
        seen = {}  # Store number -> index mapping
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
            
        return nil

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        