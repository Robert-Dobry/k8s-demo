from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1> Welcome to main page </h1>"


@app.route('/path')
def another():
    return {
        "message": "welcome to /path"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)