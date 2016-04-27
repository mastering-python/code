import setuptools

eggs = setuptools.Extension('eggs', sources=['eggs.pyx'])

if __name__ == '__main__':
    setuptools.setup(
        name='Eggs',
        version='1.0',
        ext_modules=[eggs],
        setup_requires=['Cython'],
        url='https://wol.ph/',
        author='Rick van Hattem (Wolph)',
        author_email='wolph@wol.ph',
    )

