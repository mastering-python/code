import tracemalloc


class Spam(object):
    index = 0
    cache = {}

    def __init__(self):
        Spam.index += 1
        self.cache[Spam.index] = self


class Eggs(object):
    eggs = []

    def __init__(self):
        self.eggs.append(self)


if __name__ == '__main__':
    # Initialize some variables to ignore them from the leak
    # detection
    n = 200000
    spam = Spam()

    tracemalloc.start()
    # Your application should initialize here

    snapshot_a = tracemalloc.take_snapshot()
    # This code should be the memory leaking part
    for i in range(n):
        Spam()

    Spam.cache = {}
    snapshot_b = tracemalloc.take_snapshot()
    # And optionally more leaking code here
    for i in range(n):
        a = Eggs()
        b = Eggs()
        a.b = b
        b.a = a

    Eggs.eggs = []
    snapshot_c = tracemalloc.take_snapshot()

    print('The first leak:')
    statistics = snapshot_b.compare_to(snapshot_a, 'lineno')
    for statistic in statistics[:10]:
        print(statistic)

    print('\nThe second leak:')
    statistics = snapshot_c.compare_to(snapshot_b, 'lineno')
    for statistic in statistics[:10]:
        print(statistic)

##############################################################################

import gc


class Eggs(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


# Create the objects
a = Eggs('a')
b = Eggs('b')

# Add some circular references
a.b = a
b.a = b

# Remove the objects
del a
del b

# See if the objects are still there
print('Before manual collection:')
for object_ in gc.get_objects():
    if isinstance(object_, Eggs):
        print('\t', object_, gc.get_referents(object_))

print('After manual collection:')
gc.collect()
for object_ in gc.get_objects():
    if isinstance(object_, Eggs):
        print('\t', object_, gc.get_referents(object_))

print('Thresholds:', gc.get_threshold())

##############################################################################

import gc
import collections


class Spam(object):
    index = 0
    cache = {}

    def __init__(self):
        Spam.index += 1
        self.cache[Spam.index] = self


class Eggs(object):
    eggs = []

    def __init__(self):
        self.eggs.append(self)


if __name__ == '__main__':
    n = 200000
    for i in range(n):
        Spam()

    for i in range(n):
        a = Eggs()
        b = Eggs()
        a.b = b
        b.a = a

    Spam.cache = {}
    Eggs.eggs = []
    objects = collections.Counter()
    for object_ in gc.get_objects():
        objects[type(object_)] += 1

    for object_, count in objects.most_common(5):
        print('%d: %s' % (count, object_))

##############################################################################

import gc
import weakref
import collections


class Eggs(object):
    eggs = []

    def __init__(self):
        self.eggs.append(self)


if __name__ == '__main__':
    n = 200000
    for i in range(n):
        a = Eggs()
        b = Eggs()
        a.b = weakref.ref(b)
        b.a = weakref.ref(a)

    Eggs.eggs = []
    objects = collections.Counter()
    for object_ in gc.get_objects():
        objects[type(object_)] += 1

    for object_, count in objects.most_common(5):
        print('%d: %s' % (count, object_))

##############################################################################

import weakref


class Eggs(object):
    pass


if __name__ == '__main__':
    a = Eggs()
    b = Eggs()
    a.b = weakref.ref(b)

    print(a.b())
    del b
    print(a.b())
