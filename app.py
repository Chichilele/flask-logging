from flask import Flask, request, abort
from logging.config import dictConfig


import yaml

with open("logger_config.yml") as f:
    logger_config = yaml.safe_load(f)

dictConfig(logger_config)

app = Flask(__name__)

# import declared routes
import module.module1
import module.submodule.submodule1
