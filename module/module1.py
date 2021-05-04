# from flask import current_app as app

from app import app


@app.route("/")
def index():
    app.logger.info(f"hello {__name__}")
    return f"hello {__name__}"
