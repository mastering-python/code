import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name='Our little project',
        entry_points={
            'distutils.commands': [
                'spam = 03_spam_command:SpamCommand',
            ],
        },
    )
