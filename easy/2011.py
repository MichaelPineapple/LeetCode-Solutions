""" Find Value of Variable After Performing Operations """
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            op = op.replace('X', '')
            if op[0] == '+': x += 1
            else: x -= 1
        return x