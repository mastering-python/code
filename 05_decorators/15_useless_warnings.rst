>>> import warnings
>>> import functools


>>> def ignore_warning(warning, count=None):
...     def _ignore_warning(function):
...         @functools.wraps(function)
...         def __ignore_warning(*args, **kwargs):
...             # Execute the code while recording all warnings
...             with warnings.catch_warnings(record=True) as ws:
...                 # Catch all warnings of this type
...                 warnings.simplefilter('always', warning)
...                 # Execute the function
...                 result = function(*args, **kwargs)
... 
...             # Now that all code was executed and the warnings
...             # collected, re-send all warnings that are beyond our
...             # expected number of warnings
...             if count is not None:
...                 for w in ws[count:]:
...                     warnings.showwarning(
...                         message=w.message,
...                         category=w.category,
...                         filename=w.filename,
...                         lineno=w.lineno,
...                         file=w.file,
...                         line=w.line,
...                     )
... 
...             return result
...         return __ignore_warning
...     return _ignore_warning


>>> @ignore_warning(DeprecationWarning, count=1)
... def spam():
...     warnings.warn('deprecation 1', DeprecationWarning)
...     warnings.warn('deprecation 2', DeprecationWarning)
