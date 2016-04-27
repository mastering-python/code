import setuptools

spam = setuptools.Extension('spam', sources=['spam.c'])

if __name__ == '__main__':
    setuptools.setup(
        name='Spam',
        version='1.0',
        ext_modules=[spam],
    )
