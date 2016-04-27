import os
import time
import glob
import pytest


@pytest.mark.parametrize('output_filename', glob.iglob('*/*.out'))
def test_output(xprocess, output_filename):
    output_filename = os.path.abspath(output_filename)

    def prepare(cwd):
        return '', ['python3', name + '.py']

    name, ext = os.path.splitext(output_filename)
    pid, log_file = xprocess.ensure(output_filename, prepare)

    while xprocess.getinfo(output_filename).isrunning():
        time.sleep(0.01)

    with open(output_filename) as output_file:
        assert output_file.read() == log_file.read()

