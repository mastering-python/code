import spam_10 as spam


def pytest_assertrepr_compare(config, op, left, right):
    left_spam = isinstance(left, spam.Spam)
    right_spam = isinstance(right, spam.Spam)
    if left_spam and right_spam and op == '==':
        return [
            'Comparing Spam instances:',
            '    counts: %s != %s' % (left.count, right.count),
        ]

