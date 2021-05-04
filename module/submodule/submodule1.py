from app import app

import logging

logger = logging.getLogger(__name__)


@app.route("/index2")
def index2():
    app.logger.info(f"hello {__name__}")
    logger.info("from module logger")
    return f"hello {__name__}"
