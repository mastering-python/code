from . import spam


class Eggs(spam.Spam):

    def regular_method(self):
        '''This regular method overrides
        :meth:`spam.Spam.regular_method`
        '''
        pass

