import traceback


class Spam(object):

    def run(self):
        print('Before stack print')
        traceback.print_stack()
        print('After stack print')


class Eggs(Spam):
    pass


if __name__ == '__main__':
    eggs = Eggs()
    eggs.run()

##############################################################################

import traceback


class Spam(object):

    def run(self):
        print('Before stack print')
        traceback.print_stack(limit=-1)
        print('After stack print')


class Eggs(Spam):
    pass


if __name__ == '__main__':
    eggs = Eggs()
    eggs.run()
