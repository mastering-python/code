import logging


logger = logging.getLogger(__name__)


class Spam(object):

    def __init__(self, count):
        self.logger = logger.getChild(self.__class__.__name__)

##############################################################################

import logging

logger = logging.getLogger('main_module.sub_module')
logger.addHandler(logging.FileHandler('sub_module.log'))

##############################################################################

import logging

logger = logging.getLogger('main_module.sub_module')
logger.setLevel(logging.DEBUG)

##############################################################################

import logging

logger = logging.getLogger()
exception = 'Oops...'
logger.error('Some horrible error: %r', exception)

##############################################################################

import logging

logger = logging.getLogger()
logger.error('simple error', extra=dict(spam='some spam'))

##############################################################################

import logging

logging.basicConfig(format='%(spam)s: %(message)s')
logger = logging.getLogger()
logger.error('the message', extra=dict(spam='some spam'))

##############################################################################

import logging

logger = logging.getLogger()

try:
    raise RuntimeError('Not enough spam')
except:
    logger.exception('Got an exception')

logger.error('And an error')

