""" Car Fleet """
# O(n*log[n])
class Solution(object):
    def carFleet(self, target, position, speed):
        o, m, n = 0, 0, len(position)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort(key=lambda x: x[0])
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            t = float(target - p) / float(s)
            if t > m:
                m = t
                o += 1
        return o