""" Counting Bits """
# O(n)
class Solution(object):
    def countBits(self, n):
        ans, x = [0], 1
        for i in range(1, n+1):
            if i == x * 2: x = i
            ans.append(1 + ans[i - x])
        return ans