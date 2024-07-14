""" Add Binary """
class Solution(object):
    def addBinary(self, a, b):
        an, bn = len(a), len(b)
        n = max(an, bn) + 1
        a, b, o, c = '0'*(n-an)+a, '0'*(n-bn)+b, ['0']*n, False
        for i in range(n-1, -1, -1):
            x, y = a[i] == '1', b[i] == '1'
            k = x ^ y
            o[i], c = str(int(k ^ c)), (x and y) or (c and k)
        return str(int(''.join(o)))