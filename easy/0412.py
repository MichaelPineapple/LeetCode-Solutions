""" FizzBuzz """
# O(n)?
class Solution(object):
    def fizzBuzz(self, n):
        o = []
        for x in range(1, n+1):
            s = ""
            if x % 3 == 0:
                s += "Fizz"
            if x % 5 == 0:
                s += "Buzz"
            if len(s) == 0:
                s = str(x)
            o.append(s)
        return o