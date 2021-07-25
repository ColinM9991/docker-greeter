from os import environ
from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
    name = environ.get('NAME')
    return f"Hello, my name is {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
