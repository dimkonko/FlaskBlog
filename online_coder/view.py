from flask import Blueprint, render_template
from model import OnlineCoderModel

online_coder = Blueprint("online_coder", __name__,
                      template_folder="templates")

model = OnlineCoderModel()

@online_coder.route("/online_coder")
def load():
    """Args:
        themes_list - list of themes stored on server
        dti - default theme index
    """
    return render_template("online_coder.html", themes_list=model.themes_list,
                           lang_list=model.lang_list)