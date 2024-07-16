""" Daily Temperatures """
# O(n) Time
# O(n) Space
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        o = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                pi = stack.pop()[1]
                o[pi] = i - pi
            stack.append([t, i])
        return o