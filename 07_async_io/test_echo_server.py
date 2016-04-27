def test_echo_server(xprocess):
    def prepare_server(cwd):
        return '', ['python3', '08_echo_server.py', 'server']

    def prepare_client(cwd):
        return '', ['python3', '08_echo_server.py', 'client', 3]

    server_pid, server_log_file = xprocess.ensure(
        'echo_server', prepare_server)

    client_pid, client_log_file = xprocess.ensure(
        'echo_client', prepare_client)

    xprocess.getinfo('echo_server').kill()

