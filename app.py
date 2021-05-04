from flask import Flask, request, abort
from logging.config import dictConfig

dictConfig(
    {
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
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "logconfig.log",
                "maxBytes": 1024,
                "backupCount": 3,
                "formatter": "default",
            },
        },
        "root": {"level": "INFO", "handlers": ["wsgi", "logfile"]},
    }
)

app = Flask(__name__)

# import declared routes
import module.module1
import module.submodule.submodule1
