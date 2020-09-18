from flask import Flask
from flask import render_template
from redis import Redis, RedisError
import argparse
import os
import socket

redis = Redis(host="db", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route('/')
def hello():
  try:
    visits = redis.incr("counter")
  except RedisError:
    visits = "<i>Cannot connect to Redis host 'db'</i>"

  return render_template('index.html', hostname=socket.gethostname(),vcount=visits)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

