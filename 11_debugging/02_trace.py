def eggs_generator():
    yield 'eggs'
    yield 'EGGS!'


def spam_generator():
    yield 'spam'
    yield 'spam!'
    yield 'SPAM!'

generator = spam_generator()
print(next(generator))
print(next(generator))

generator = eggs_generator()
print(next(generator))

##############################################################################

import sys
import trace as trace_module
import contextlib


@contextlib.contextmanager
def trace(count=False, trace=True, timing=True):
    tracer = trace_module.Trace(
        count=count, trace=trace, timing=timing)
    sys.settrace(tracer.globaltrace)
    yield tracer
    sys.settrace(None)

    result = tracer.results()
    result.write_results(show_missing=False, summary=True)


def eggs_generator():
    yield 'eggs'
    yield 'EGGS!'


def spam_generator():
    yield 'spam'
    yield 'spam!'
    yield 'SPAM!'


with trace():
    generator = spam_generator()
    print(next(generator))
    print(next(generator))

generator = eggs_generator()
print(next(generator))
