""" Search In Rotated Sorted Array """
# This problem was a nightmare, and my code is horrendous.
# O(log[n])
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            lv, rv = nums[l], nums[r]
            m = (l + r) // 2
            mv = nums[m]
            if lv > rv:
                if lv > mv:
                    if mv > target: r = m - 1
                    elif mv < target:
                        if target > lv: r = m - 1
                        elif target < lv: l = m + 1
                        else: return l
                    else: return m
                elif lv < mv:
                    if mv < target: l = m + 1
                    elif mv > target:
                        if target > lv: r = m - 1
                        elif target < lv: l = m + 1
                        else: return l
                    else: return m
                else:
                    if lv == target: return l
                    elif rv == target: return r
                    else: return -1
            elif lv < rv:
                if mv > target: r = m - 1
                elif mv < target: l = m + 1
                else: return m
            else:
                if lv == target: return l
                else: return -1
        return -1