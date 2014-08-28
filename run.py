from flask import Flask
from main_page.view import main_page
from online_coder.view import online_coder

app = Flask(__name__)
app.register_blueprint(main_page)
app.register_blueprint(online_coder)


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)