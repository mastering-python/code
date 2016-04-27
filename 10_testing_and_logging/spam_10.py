
class Spam(object):

    def __init__(self, count):
        self.count = count

    def __eq__(self, other):
        return self.count == other.count

