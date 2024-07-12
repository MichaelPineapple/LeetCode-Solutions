""" Majority Element II """
class Solution(object):
    def majorityElement(self, nums):
        o, m = [], {}
        k = len(nums)//3
        for n in nums:
            x = m.get(n, 0)
            m[n] = x + 1
            if x == k:
                o.append(n)
        return o
        # Nice!