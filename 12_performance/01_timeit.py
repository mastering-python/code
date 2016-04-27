import timeit


def test_list():
    return list(range(10000))


def test_list_comprehension():
    return [i for i in range(10000)]


def test_append():
    x = []
    for i in range(10000):
        x.append(i)

    return x


def test_insert():
    x = []
    for i in range(10000):
        x.insert(0, i)

    return x


def benchmark(function, number=100, repeat=10):
    # Measure the execution times
    times = timeit.repeat(function, number=number, globals=globals())
    # The repeat function gives `repeat` results so we take the min()
    # and divide it by the number of runs
    time = min(times) / number
    print('%d loops, best of %d: %9.6fs :: %s' % (
        number, repeat, time, function))


if __name__ == '__main__':
    benchmark('test_list()')
    benchmark('test_list_comprehension()')
    benchmark('test_append()')
    benchmark('test_insert()')

##############################################################################

import timeit

timeit.main(args=['[x for x in range(1000000)]'])
