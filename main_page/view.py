from flask import Blueprint, render_template, request, redirect
from model import MainModel

main_page = Blueprint("main_page", __name__,
                      template_folder="templates")

model = MainModel()

@main_page.route("/")
def index():
    return render_template("blog.html", posts_list=model.get_all())

@main_page.route("/about")
def about():
    return "About page"

@main_page.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        model.add_post(request.form)
        return redirect("/")
    return render_template("add_post.html")

