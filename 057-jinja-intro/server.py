from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    random_num = (random.randint(1, 10))
    current_year = datetime.now().year
    return render_template('index.html', rand_num=random_num, year=current_year)


@app.route("/guess/<name>")
def guess(name: str):
    gender = requests.get(url=f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(url=f"https://api.agify.io?name={name}").json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def show_blog(num):
    print(f"Check log to prove param is passed from link on index.html: {num}")
    all_posts = requests.get(url="https://jsonplaceholder.typicode.com/users/1/posts").json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    # Running in debug mode auto-reloads when file changes
    app.run(debug=True)