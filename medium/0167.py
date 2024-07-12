""" Two Sum II - Input Array is Sorted """
# O(n) Time
# O(1) Space
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t > target:
                r -= 1
            elif t < target:
                l += 1
            else:
                return [l+1, r+1]
        return []