from multiprocessing import managers
constants = __import__('05_remote_processor')


manager = managers.BaseManager(
    address=(constants.host, constants.port),
    authkey=constants.password)
manager.register('queue')
manager.connect()

queue = manager.queue()
for i in range(1000):
    queue.put(i)

