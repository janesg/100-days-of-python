from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def simple_static_render():
    return render_template('index.html')


if __name__ == "__main__":
    # Running in debug mode auto-reloads when file changes
    app.run(debug=True)