import setuptools

spam = setuptools.Extension('spam', sources=['07_python.c'])

if __name__ == '__main__':
    setuptools.setup(
        name='Spam',
        version='1.0',
        ext_modules=[spam],
    )

