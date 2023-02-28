from flask import Flask,jsonify
from flask import request
app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello Harsh"

if __name__=="main":
    app.run(host="0.0.0.0")