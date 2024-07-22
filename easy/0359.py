""" Logger Rate Limiter """
class Logger(object):

    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.log:
            t = self.log[message]
            if timestamp < t: return False
        self.log[message] = timestamp + 10
        return True