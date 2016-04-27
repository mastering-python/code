import os
import json
from logging import config

json_filename = os.path.join(os.path.dirname(__file__),
                             '18_logging_json_config.json')
with open(json_filename) as fh:
    config.dictConfig(json.load(fh))


