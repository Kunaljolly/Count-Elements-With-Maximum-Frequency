class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = 0
        c = Counter(nums)
        for x in set(nums):
            if nums.count(x) == max(c.values()):
                ma += nums.count(x)
        return ma


