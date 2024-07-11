""" Jump Game """
# O(n) Time
# O(1) Space
class Solution(object):
    def canJump(self, nums):
        for i in range(len(nums)-1):
            n = nums[i]
            if n == 0:
                j = i
                b = False
                while j >= 0:
                    if j+nums[j] > i:
                        b = True
                        break
                    j -= 1
                if not b:
                    return False
        return True