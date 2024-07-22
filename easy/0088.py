""" Merge Sorted Array """
# O(n)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1
        k = m + n - 1
        while k > i >= 0:
            x, y = nums1[i], nums2[j]
            if x > y:
                nums1[k] = x
                i -= 1
            else:
                nums1[k] = y
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1