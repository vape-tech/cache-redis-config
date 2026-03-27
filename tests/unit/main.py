# main.py

import os
import logging
from flask import Flask
from flask_redis import FlaskRedis

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['REDIS_URL'] = os.environ.get('REDIS_URL')

# Add redis extension
redis_store = FlaskRedis(app)

# Define routes
@app.route('/')
def index():
    return 'Cache Redis Config API'

@app.route('/get_key/<string:key>')
def get_key(key):
    value = redis_store.get(key)
    return value

@app.route('/set_key/<string:key>/<string:value>')
def set_key(key, value):
    redis_store.setex(key, value, 60)  # Set value with 1 minute TTL
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)