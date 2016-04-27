import sys
import timeit

try:
    import spam
except ImportError:
    print('This example requires you to build the spam module first')
    print('Run: python 07_setup.py build')
else:
    def sum_of_squares(n):
        sum = 0

        for i in range(n):
            if i * i < n:
                sum += i * i
            else:
                break

        return sum

    if __name__ == '__main__':
        if not sys.argv[2:] or not all(a.isdigit() for a in sys.argv[1:]):
            print('%s requires 2 numeric arguments' % sys.argv[0])
            print('Try: %s 1000 10000000' % sys.argv[0])
            sys.exit(1)

        c = int(sys.argv[1])
        n = int(sys.argv[2])

        print('%d executions with n: %d' % (c, n))
        print('C sum of squares: %d took %.3f seconds' % (
            spam.sum_of_squares(n),
            timeit.timeit('spam.sum_of_squares(n)', number=c,
                          globals=globals()),
        ))
        print('Python sum of squares: %d took %.3f seconds' % (
            sum_of_squares(n),
            timeit.timeit('sum_of_squares(n)', number=c,
                          globals=globals()),
        ))

