import os
import re
import platform

from flask import Flask
from blueprints.user import user
from blueprints.event import event
from utils.logger import get_logger, get_flask_log_handler
from utils.config import get_config

app = Flask(__name__)

app.register_blueprint(user.routes, url_prefix='/user')
app.register_blueprint(event.routes, url_prefix='/event')
app.secret_key = get_config()['app_secret']

@app.route('/')
def index():
    string = get_config()['database']['url']
    if string is None:
        db_path = "No Database configuration..."
    else:
        db_path = re.search('(?<=@).*', string).group(0)
    return """
        <h1>Server started...</h1>
        <h2>Python version: %s<h2>
        <h2>Database: %s</h2>
    """ % (platform.python_version(), db_path)



if __name__ == '__main__':
    get_logger().info("App started...")
    app.run(host='0.0.0.0', debug=True)

