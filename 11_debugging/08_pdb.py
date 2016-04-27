import pdb


def spam():
    eggs = 123
    print('The begin of spam')
    pdb.set_trace()
    print('The end of spam')
    print('The value of eggs: %s' % eggs)


if __name__ == '__main__':
    spam()

##############################################################################

import pdb


def spam(eggs):
    print('eggs:', eggs)


if __name__ == '__main__':
    pdb.set_trace()
    for i in range(5):
        spam(i)
