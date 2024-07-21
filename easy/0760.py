""" Find Anagram Mappings """
class Solution(object):
    def anagramMappings(self, nums1, nums2):
        n = len(nums1)
        out = []
        for i in range(n):
            x = nums1[i]
            for j in range(n):
                y = nums2[j]
                if x == y:
                    out.append(j)
                    break
        return out