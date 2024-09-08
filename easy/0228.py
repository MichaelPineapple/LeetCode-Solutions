""" Summary Ranges """
class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0: return []
        nums.append(float('inf'))
        o = []
        p = b = nums[0]
        for x in nums:
            if x > p + 1:
                s = str(b)
                if p != b: s += "->"+str(p)
                o.append(s)
                b = x
            p = x
        return o