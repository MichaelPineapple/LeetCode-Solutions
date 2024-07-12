""" Threesome """
# O(n^2) Time
# O(n)   Space
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        o = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            k = -a
            l, r = i+1, n - 1
            while l < r:
                b = nums[l]
                if l > i + 1 and b == nums[l-1]:
                    l += 1
                    continue
                c = nums[r]
                if r < n - 1 and c == nums[r+1]:
                    r -= 1
                    continue
                t = b + c
                if t > k:
                    r -= 1
                else:
                    if t == k:
                        o.append([a, b, c])
                    l += 1
        return o
