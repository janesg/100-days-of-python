from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_italicised(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper


@app.route("/")
def home():
    return "Nothing to see here!"


# show use of path variables and type converters
@app.route("/greet/<name>/<int:age>")
def greeter(name, age):
    return f"Hi there {name}... are you really {age * 7} in dog years ?"


@app.route("/bye")
@make_bold
@make_italicised
@make_underlined
def goodbye():
    return "Bye!"


if __name__ == "__main__":
    # Running in debug mode auto-reloads when file changes
    app.run(debug=True)