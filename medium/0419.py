""" Battleships in a Board """
class Solution(object):
    def countBattleships(self, board):
        o = 0
        vship = {}
        for i, row in enumerate(board):
            row.append('.')
            count = 0
            for j, x in enumerate(row):
                if x == 'X':
                    if count == 1: o += 1
                    count += 1
                else:
                    if count == 1:
                        k = j - 1
                        q = vship.get(k, -2)
                        if q != i - 1: o += 1
                        vship[k] = i
                    count = 0
        return o