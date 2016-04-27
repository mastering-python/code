>>> import asyncio


>>> async def sleeper(delay):
...     await asyncio.sleep(delay)
...     print('Finished sleeper with delay: %.1f' % delay)

# Create an event loop
>>> loop = asyncio.get_event_loop()

# Create the task
>>> result = loop.call_soon(loop.create_task, sleeper(0.1))

# Make sure the loop stops after 0.2 seconds
>>> result = loop.call_later(0.2, loop.stop)

# Start the loop and make it run forever. Or at least until the loop.stop gets
# called in 0.2 seconds.
>>> loop.run_forever()
Finished sleeper with delay: 0.1

##############################################################################

>>> import asyncio


>>> async def stack_printer():
...     for task in asyncio.Task.all_tasks():
...         task.print_stack()

# Create an event loop
>>> loop = asyncio.get_event_loop()

# Create the task
>>> result = loop.run_until_complete(stack_printer())
Stack for <Task pending ...

