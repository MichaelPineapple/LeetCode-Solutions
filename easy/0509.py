""" Fibonacci Number """
# Time O(?)
# Space O(?)
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1)+self.fib(n - 2)