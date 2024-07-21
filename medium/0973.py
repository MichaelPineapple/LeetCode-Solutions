import math

""" K Closest Points To Origin """
# O(n*log[n])
class Solution(object):
    def kClosest(self, points, k):
        distances = []
        for i, p in enumerate(points):
            x, y = p[0], p[1]
            d = math.sqrt((x*x) + (y*y))
            distances.append([d, i])
        distances = sorted(distances, key=lambda x: x[0])[:k]
        return [points[d[1]] for d in distances]

# Simplified
class Solution(object):
    def kClosest(self, points, k):
        def dist(p):
            return math.sqrt((p[0]**2) + (p[1]**2))
        points.sort(key=dist)
        return points[:k]