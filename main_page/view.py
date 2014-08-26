from flask import Blueprint, render_template

main_page = Blueprint("main_page", __name__,
                      template_folder="templates")

@main_page.route("/")
def lol():
    return render_template("blog.html")

@main_page.route("/about")
def about():
    return "About page"