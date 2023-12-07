class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [1]*len(nums)
        pr = 1
        for i in range(0,len(nums)-1):
            pr = pr*nums[i]
            out[i+1]=pr

        pos = 1
        print(out)
        for i in range(len(out)):
            out[len(nums)-1-i]*=pos
            pos=pos*nums[len(nums)-1-i]

        return out
