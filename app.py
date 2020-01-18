from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

if __name__== '__main':
    app.run()
