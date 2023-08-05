from flask import Blueprint, url_for
from flask import request
from flask import redirect
from flask import flash
from flask import render_template
from werkzeug.exceptions import NotFound, BadRequest

from models import Post, db
from .forms.posts import PostForm

posts_app = Blueprint("posts_app", __name__, url_prefix="posts")




@posts_app.get("/", endpoint="posts")
def get_post_list():
    posts: list[Post] = Post.query.order_by(Post.id).all()
    return render_template("posts.html", posts=posts)


def get_post_by_id(post_id: int) -> Post:
    return Post.query.get_or_404(
        post_id, description=f"Post #{post_id} not found!"
    )


@posts_app.get("/<int:post_id>/", endpoint="details")
def get_post_details(post_id: int):
    post = get_post_by_id(post_id=post_id)
    return render_template("details.html", post=post)


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("add.html", form=form)

    if not form.validate_on_submit():
        return render_template("add.html", form=form), 400

    post = Post(title=form.data["title"], body=form.data["body"])
    db.session.add(post)
    db.session.commit()
    url = url_for("posts_app.details", post_id=post.id)
    flash(f"Created post {post.title!r}", category="success")
    return redirect(url)


@posts_app.route(
    "/<int:post_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_post(post_id: int):
    post = get_post_by_id(post_id=post_id)
    if request.method == "GET":
        return render_template("confirm-delete.html", post=post)
    post_title = post.title
    post_id = post.id
    db.session.delete(post)
    db.session.commit()
    flash(f"Deleted post #{post_id} {post_title!r}", category="danger")
    url = url_for("posts_app.posts")
    return redirect(url)



