from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>BYE!</p>"


if __name__ == "__main__":
    app.run()