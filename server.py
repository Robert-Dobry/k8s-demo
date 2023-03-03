from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/path')
def another():
    return {
        "message": "welcome to /path"
    }


if __name__ == "__main__":
    app.run()
