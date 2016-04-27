def receive():
    import time
    import logging
    from logging import config

    listener = config.listen()
    listener.start()

    try:
        while True:
            logging.debug('debug')
            logging.info('info')
            some_logger = logging.getLogger('some')
            some_logger.warning('warning')
            some_logger.error('error')
            other_logger = some_logger.getChild('other')
            other_logger.critical('critical')

            time.sleep(5)

    except KeyboardInterrupt:
        # Stop listening and finish the listening thread
        logging.config.stopListening()
        listener.join()


def send():
    import os
    import struct
    import socket
    from logging import config

    ini_filename = os.path.join(os.path.dirname(__file__),
                                '20_logging_network_config.ini')
    with open(ini_filename) as fh:
        data = fh.read()

    # Open the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    sock.connect(('127.0.0.1', config.DEFAULT_LOGGING_CONFIG_PORT))
    # Send the magic logging packet
    sock.send(struct.pack('>L', len(data)))
    # Send the config
    sock.send(data)
    # And close the connection again
    sock.close()

