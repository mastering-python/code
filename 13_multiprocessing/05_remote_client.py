from multiprocessing import managers
constants = __import__('05_remote_processor')


manager = managers.BaseManager(
    address=(constants.host, constants.port),
    authkey=constants.password)
manager.register('queue')
manager.register('primes')
manager.connect()

queue = manager.queue()
while not queue.empty():
    print(manager.primes(queue.get()))

