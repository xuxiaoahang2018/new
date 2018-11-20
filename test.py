#! /home/xuxiaohang/.pyenv/shims/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "welcome index"

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="8080")
