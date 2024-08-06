from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_func():
        return f"<b>{func()}</b>"
    return wrapper_func


def make_emphasis(func):
    def wrapper_func():
        return f"<em>{func()}</em>"
    return wrapper_func

def make_underline(func):
    def wrapper_func():
        return f"<u>{func()}</u>"
    return wrapper_func

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
        "<p>This is my paragraph</p>" \
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjF1Y3J6b2Z6c25nem9lMng0MmJ3NXQ0bnpkOWpzY2V3OXNwNG4zeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif'>"
    


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)