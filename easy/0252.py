""" Meeting Rooms """
# O(n*log[n])
class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        prevEnd = 0
        for start, end in intervals:
            if start < prevEnd: return False
            prevEnd = end
        return True