import asyncio


@asyncio.coroutine
def printer():
    print('This is a coroutine')

printer()

##############################################################################

import asyncio
import logging


logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()
