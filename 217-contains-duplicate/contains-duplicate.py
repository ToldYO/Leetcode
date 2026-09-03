class Solution(object):
    def containsDuplicate(self, nums):

        seen={}
        for i in nums:
            seen[i]=seen.get(i)

        return len(nums) != len(set(nums))
        """

        :type nums: List[int]
        :rtype: bool
        """
        