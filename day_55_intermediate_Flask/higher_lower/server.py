from flask import Flask
import random

app = Flask(__name__)


# def check_number(func):
#     def wrapper(*args):



@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


random_num = random.randint(0, 9)

@app.route("/<int:number>")
def greet(number):
    if random_num == number:
        return f"<h1>You Found me</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif random_num < number:
        return f"<h1> Too high, try again! </h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif random_num > number:
        return f"<h1> Too low, try again! </h1>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        


if __name__ == "__main__":
    app.run(debug=True)