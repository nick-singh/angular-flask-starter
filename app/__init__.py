from flask import Flask, jsonify, request
import sys


app_base = '/api'
app = Flask(__name__, static_url_path = "")
@app.route('/')
def root(): 
  return app.send_static_file('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)