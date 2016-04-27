import asyncio


@asyncio.coroutine
def sleeper():
    yield from asyncio.sleep(0.1)

##############################################################################

async def some_coroutine():
    pass

##############################################################################

import asyncio


@asyncio.coroutine
def some_coroutine():
    pass

##############################################################################

import asyncio


async def sleeper():
    await asyncio.sleep(0.1)
