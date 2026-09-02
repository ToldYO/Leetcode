class Solution(object):
    def majorityElement(self, nums):

        set={}
        res=0
        for i in nums:
            set[i]=set.get(i,0)+1
            res=max(set,key=set.get)
            
        return res

            
            

        """
        :type nums: List[int]
        :rtype: int
        """
        