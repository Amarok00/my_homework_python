from os import getenv

import requests

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from models import db, Post
from views.posts import posts_app 
import config 

POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

app = Flask(__name__)
app.register_blueprint(posts_app,url_prefix=("/posts/"))

csrf = CSRFProtect(app)

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
class_object = f"config.{config_class_name}"
app.config.from_object(class_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)


@app.get("/")
def hello_root():
    return render_template("index.html")


@app.get("/about/")
def about_us():
    return render_template("about.html")

def fetch_posts_data() -> list[dict]:
    response=requests.get(POSTS_DATA_URL)
    data = response.json()
    return data

@app.get("/placeholder/",endpoint="placeholder")
def get_json_list():
    posts_data = fetch_posts_data()
    return render_template("placeholder.html",posts_data=posts_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
