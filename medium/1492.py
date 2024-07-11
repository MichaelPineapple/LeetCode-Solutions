""" The Kth Factor of N """
class Solution(object):
    def kthFactor(self, n, k):
        j = 1
        for i in range(1, n + 1):
            if n % i == 0:
                if j == k:
                    return i
                j += 1
        return -1
