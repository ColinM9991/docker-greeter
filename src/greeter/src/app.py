from os import environ
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def greet():
    name = environ.get('NAME')
    referrer = request.headers['X-Referrer']
    return f"Hello, I'm {name}, brought to you by {referrer}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
