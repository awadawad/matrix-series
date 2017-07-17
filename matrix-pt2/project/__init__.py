# project/__init__.py

from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/matrix', methods=['GET'])
def matrix():
    return jsonify({
        'hello': 'world'
    })
