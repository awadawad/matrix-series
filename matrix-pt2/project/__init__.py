# project/__init__.py

import os
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/matrix', methods=['GET'])
def matrix():
    return jsonify({
        'hello': 'world'
    })
