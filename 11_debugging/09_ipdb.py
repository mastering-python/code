import ipdb


def spam(eggs):
    print('eggs:', eggs)


if __name__ == '__main__':
    ipdb.set_trace()
    for i in range(3):
        spam(i)

##############################################################################

import ipdb


def main():
    pass


with ipdb.launch_ipdb_on_exception():
    main()
