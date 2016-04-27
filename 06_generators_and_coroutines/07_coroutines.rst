Most of the contextlib functions have extensive documentation available in the Python manual. ExitStack in particular is documented using many examples: https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack. I would recommend keeping an eye on the contextlib documentation as it is improving greatly with every Python version.
Coroutines
Coroutines are subroutines that offer non-preemtive multitasking through multiple entry points. The basic premise is that coroutines allow for two functions to communicate with each other while running. Normally, this type of communication is reserved only for multitasking solutions but coroutines offer a relatively simple way of achieving this at almost no added performance cost.
Since generators are lazy by default the workings of coroutines are fairly obvious. Until a result is consumed the generator sleeps, but while consuming a result the generator becomes active. The difference between regular generators and coroutines is that coroutines don't simply return values to the calling function, but they can receive values as well.
Basic example
In the previous paragraphs we have seen how regular generators can yield values. But that's not all generators can do, they can actually receive values as well. The basic usage is fairly simple:
>>> def generator():
...     value = yield 'spam'
...     print('Generator received: %s' % value)
...     yield 'Previous value: %r' % value

>>> g = generator()
>>> print('Result from generator: %s' % next(g))
Result from generator: spam
>>> print(g.send('eggs'))
Generator received: eggs
Previous value: 'eggs'
