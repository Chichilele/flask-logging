from logging.config import dictConfig

# import json
import logging

# import time

# time.sleep(2)

for name in logging.root.manager.loggerDict:
    print("***NAME: ", name)


import yaml

# with open("logger_config.yaml") as f:
#     logger_config = yaml.safe_load(f)

# with open("logger_config.json") as f:
#     logger_config = json.load(f)
# dictConfig(logger_config)


# werkzeug_logger = logging.getLogger("werkzeug")

import werkzeug

print("before:", werkzeug._internal._logger)
# werkzeug._internal._logger.removeHandler(werkzeug._internal._logger.handlers[0])
# werkzeug._internal._logger.setLevel(logging.NOTSET)
# werkzeug._internal._logger = None
print("after:", werkzeug._internal._logger)


dictConfig(
    {
        # "disable_existing_loggers": False,
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(name)s of %(module)s : %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            },
            "logfile": {
                "class": "logging.FileHandler",
                "filename": "logconfig.log",
                "formatter": "default",
            },
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {"level": "INFO", "handlers": ["console", "logfile"]},
    }
)

werkzeug._internal._log("info", "hello")

from flask import Flask, abort, request

app = Flask(__name__)

# import declared routes
import module.module1
import module.submodule.submodule1
