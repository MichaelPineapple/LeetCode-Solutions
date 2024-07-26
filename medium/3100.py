""" Water Bottles II """
# O(n)
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        drankBottles = 0
        emptyBottles = 0

        while True:
            if emptyBottles < numExchange:
                if numBottles > 0:
                    emptyBottles += numBottles
                    drankBottles += numBottles
                    numBottles = 0
                else:
                    break
            else:
                emptyBottles -= numExchange
                numExchange += 1
                numBottles += 1

        return drankBottles