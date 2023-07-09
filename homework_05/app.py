from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


app.config.update(SECRET_KEY="34d27865d50a5c1f8d8e0b8fcdf378da")


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def get_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
