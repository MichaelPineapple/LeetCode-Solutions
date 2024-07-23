""" Remove Duplicates From Sorted Array """
class Solution(object):
    def removeDuplicates(self, nums):
        i, k, p = 0, 0, nums[0]-1
        while i < len(nums):
            x = nums[i]
            if x == p:
                del nums[i]
            else:
                p = x
                k += 1
                i += 1
        return k


# Maybe better solution without deletion
# 00:32
class Solution0(object):
    def removeDuplicates(self, nums):
        n, s, j, b = len(nums), set(), 0, None
        for i in range(n):
            if b is not None: nums[i] = b
            if j == n: break
            s.add(nums[i])
            while j < n:
                y = nums[j]
                if y not in s:
                    b = y
                    break
                j += 1
        return len(s)