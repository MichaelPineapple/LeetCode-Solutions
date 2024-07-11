""" Flipping An Image """
# Time O(?)
# Space O(?)
class Solution(object):
    def flipAndInvertImage(self, image):
        out = []
        for r in image:
            t = []
            for i in range(len(r)-1, -1, -1):
                v = r[i]
                if v == 0:
                    v = 1
                else:
                    v = 0
                t.append(v)
            out.append(t)
        print(out)
        return out