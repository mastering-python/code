import os
from logging import config

config.fileConfig(os.path.join(os.path.dirname(__file__),
                  '19_logging_ini_config.ini'))
