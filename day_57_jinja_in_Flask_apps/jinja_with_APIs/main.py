from flask import Flask, render_template
import random
from datetime import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1,10)
    my_name = "Michael Collazos"
    year = datetime.now().year

    return render_template('index.html', num=random_num, year=year, my_name = my_name)


@app.route("/guess/<name>")
def guess(name):

    parameters = {"name": name}
    response = requests.get(url="https://api.genderize.io", params=parameters)
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]

    parameters = {"name": name}
    response = requests.get(url="https://api.agify.io", params=parameters)
    response.raise_for_status()
    data = response.json()
    age = data["age"]
    return render_template('guess.html', name = name, gender = gender, age = age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    data = blog_response.json()

    return render_template('blog.html', posts = data)


if __name__ == "__main__":
    app.run(debug=True)


