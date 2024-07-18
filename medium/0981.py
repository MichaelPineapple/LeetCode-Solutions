""" Time Based Key-Value Store """
class TimeMap(object):

    def __init__(self):
        self.data = {}

    # O(1)
    def set(self, key, value, timestamp):
        if key not in self.data: self.data[key] = []
        self.data[key].append([value, timestamp])

    # O(log[n])
    def get(self, key, timestamp):
        o = ""
        d = self.data.get(key, [])
        l, r = 0, len(d) - 1
        while l <= r:
            m = (l + r) // 2
            mv, mt = d[m]
            if mt > timestamp:
                r = m - 1
            elif mt < timestamp:
                l, o = m + 1, mv
            else:
                return mv
        return o